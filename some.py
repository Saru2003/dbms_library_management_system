import streamlit as st
from pymongo import MongoClient
import time
import pandas as pd
client=MongoClient("mongodb+srv://sarvesh:sarvesh@cluster0.fi6cwh7.mongodb.net/?retryWrites=true&w=majority")
db=client.get_database('database')
records1=db.lib_1
st.set_page_config(page_title="Library",layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.write(
    '''<style>
    .my-div {
        position: relative;
    }
    .my-div::after {
        content: "";
        position: absolute;
        top: 0.5;
        bottom: 0.5;
        width: 0.5px;
        border-right: 15px solid white;
        margin-left: 45%;
        height: 600px;
    }
</style>
<div class="my-div">
    
</div>
''',unsafe_allow_html=True)
page_bg="""
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://api.time.com/wp-content/uploads/2021/10/GettyImages-577674005.jpg");
    background-size: cover;
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
</style>
"""

# st.markdown(page_bg,unsafe_allow_html=True)
c1,c2,c3=st.columns([1.5,0.5,2])
with c1:
    # st.write('''<h4 style="font-family:georgia,garamond,serif;font-size:90px"><span style="color: white">Library</span></h3>''',unsafe_allow_html=True)
    # st.write('''<h4 style="font-family:georgia,garamond,serif;font-size:90px"><span style="color: white">Management</span></h3>''',unsafe_allow_html=True)
    # st.write('''<h4 style="font-family:georgia,garamond,serif;font-size:90px"><span style="color: white">Systems</span></h3>''',unsafe_allow_html=True)
    st.write("<h4>Select the operation</h4>",unsafe_allow_html=True)
    e=st.selectbox("",options=["--Choose--","Add Book","Borrow","Return","Show Books","Update"])
tabs_font_css = """
<style>
div[class*="stTextArea"] label {
  font-size: 10px;
  color: red;
}

div[class*="stTextInput"] label {
  font-size: 10px;
  color: white;
}

div[class*="stNumberInput"] label {
  font-size: 10px;
  color: green;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

with c3:
    if e=="Add Book":
        isbn=st.text_input("ISBN")
        title=st.text_input("Title")
        price=st.text_input("Price")
        pub_id=st.text_input("Publication ID")
        author=st.text_input("Author")
        category=st.text_input("Category")
        qty=st.text_input("Quantity")
        if st.button("Submit"):
            isbn_err=price_err=qty_err=0
            if isbn in [" ",""]:
                st.error("Enter valid ISBN number")
            else:
                isbn_err=1
            if not price.isdigit():
                st.error("Enter valid price")
            else:
                price_err=1
            if not qty.isdigit():
                st.error("Enter valid quantity")
            else:
                qty_err=1
            if isbn_err==price_err==qty_err==1:
                    new_rec={'isbn':isbn,'title':title,'price':int(price),'pub_id':pub_id,'author':author,'category':category,'qty':int(qty)}
                    with st.spinner("Adding book"):
                        time.sleep(2)
                        records1.insert_one(new_rec)
                    st.success("Done")
    if e=="Show Books":
        # st.write("jj")
        id=[]
        isbn=[]
        title=[]
        price=[]
        pub_id=[]
        author=[]
        category=[]
        quantity=[]
        for i in records1.find():
            id.append([i["_id"]])
            isbn.append(i["isbn"])
            title.append(i["title"])
            price.append(i["price"])
            pub_id.append(i["pub_id"])
            author.append(i["author"])
            category.append(i["category"])
            quantity.append(i["qty"])
        # st.checkbox("Use container width", value=False, key="use_container_width")

        data = {
            "ISBN": isbn,
            "Title": title,
            "Price": price,
            "Publication ID": pub_id,
            "Author": author,
            "Category": category,
            "Quantity": quantity
        }

        df = pd.DataFrame(data)
        df.index += 1
        df.index.name = 'Row'
        st.dataframe(df)
    if e=="Update":
        isbn_arr=[]
        for i in records1.find():
            isbn_arr.append(i["isbn"])
        isbn=st.text_input("Enter ISBN")
        qty_=st.text_input("Update to")
        if st.button("Update"):
            if qty_.isdigit():
                if isbn in isbn_arr:
                    myquery = {"isbn":isbn}        
                    newvalues = {"$set":{"qty":int(qty_)}}
                    records1.update_many(myquery, newvalues)
                    st.success("Updated!")
                else:
                    st.error("Enter valid ISBN number")
            else:
                st.error("Enter valid quantity")
    if e=="Borrow":
        records2 = db.lib_2
        isbn_arr=[]
        title_arr=[]
        for i in records1.find():
            isbn_arr.append(i["isbn"])
            title_arr.append(i["title"])
        isbn_=st.text_input("Enter ISBN")
        user_id=st.text_input("Enter User ID")
        if st.button("Proceed"):
            if isbn_ in isbn_arr:
                index=isbn_arr.index(isbn_)
                query={"user_id": user_id}
                new_book={
                    "isbn":isbn_,
                    "title":title_arr[index]
                }

                myquery = {"isbn":isbn_}
                
                qty_=records1.find_one({"isbn":isbn_},{"_id": 0, "qty": 1})
                newvalues = {"$set":{"qty":int(qty_['qty'])-1}}
                records1.update_many(myquery, newvalues)

                # st.write(isbn_,title_arr[index])

                query = {"user_id": int(user_id)}
                update={"$push": {"books": new_book}}
                records2.update_one(query, update)
                # update = {"$push": {"books": new_book}}
                # records2.update_one(query, update)
                # st.write("ok2")
                st.success("Borrow process completed")
            else:
                st.error("Enter Valid ISBN")
    if e=="Return":
        records2 = db.lib_2
        isbn_arr=[]
        # title_arr=[]
        for i in records1.find():
            isbn_arr.append(i["isbn"])
            # title_arr.append(i["title"])
        isbn_=st.text_input("Enter ISBN")
        user_id=st.text_input("Enter User ID")
        if st.button("Proceed"):
            if isbn_ in isbn_arr:
                # index=isbn_arr.index(isbn_)
                myquery = {"isbn":isbn_}
                qty_=records1.find_one({"isbn":isbn_},{"_id": 0, "qty": 1})
                newvalues = {"$set":{"qty":int(qty_['qty'])+1}}
                records1.update_many(myquery, newvalues)

                query={"user_id": int(user_id)}
                update = {"$pull": {"books": {"isbn":isbn_}}}
                records2.update_one(query, update)
                st.success("Return process completed")
            else:
                st.error("Enter Valid ISBN")
    # st.write("<h5>Enter your login credentials</h5>",unsafe_allow_html=True)