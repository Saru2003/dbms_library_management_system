from pymongo import MongoClient
import pandas as pd
client = MongoClient("mongodb+srv://sarvesh:sarvesh@cluster0.fi6cwh7.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database('database')
records1 = db.lib_1
records2= db.lib_2
# isbn_="fghj"
# try:
#     query = {"user_id": 105}

#     # retrieve the user document
#     user_document = records2.find_one(query)

#     # access the password field from the user document
#     password = user_document["pass"]
#     print(password)
# except TypeError:
#     print("blah")
id=[]
isbn=[]
title=[]
price=[]
pub_id=[]
author=[]
category=[]
quantity=[]
for i in records1.find():
    if 'w' in i["title"]:
        id.append([i["_id"]])
        isbn.append(i["isbn"])
        title.append(i["title"])
        price.append(i["price"])
        pub_id.append(i["pub_id"])
        author.append(i["author"])
        category.append(i["category"])
        quantity.append(i["qty"])
# st.checkbox("Use container width", value=False, key="use_container_width")
print(title)
data = {
    "ISBN": isbn,
    "Title": title,
    "Price": price,
    "Publication ID": pub_id,
    "Author": author,
    "Category": category,
    "Quantity": quantity
}

# df = pd.DataFrame(data)
# df.index += 1
# df.index.name = 'Row'
# st.dataframe(df)
# query = {"user_id": 101}
# retrieve the user document
# user_document = records2.find_one(query)
# pipeline = [
#     {"$match": query},
#     {"$project": {"values": {"$map": {"input": "$books", "as": "b", "in": "$$b.isbn"}}}}
# ]

# execute the aggregation pipeline and retrieve the result
# result = list(records2.aggregate(pipeline))[0]

# access the isbn values from the result dictionary
# isbn_values = result["values"]

# print(isbn_values)
# access the books field from the user document
# books = user_document["books"]

# print(user_document['books.isbn'])
# qty_=records1.find_one({"isbn":isbn_},{"_id": 0, "qty": 1})
# print(qty_['qty'])
'''
query={"user_id": 101}
new_book={
    "title":"some1",
    "some":"op"
}
update = {"$pull": {"books": new_book}}
records2.update_one(query, update)
query = {"user_id": 101}
update={"$push": {"books": new_book}}
records2.update_one(query, update)
'''
# retrieve the user document
# user_document = records2.find_one(query)

# access the author of the first book in the books array
# author = user_document["books"][0]
# print(author)
# records2.update_one({"user_id":101},{"$set":{"books":books+"jo"}})
# print(records2.estimated_document_count())
# new_rec = {'name': 'c', 'age': 20}
# records.insert_one(new_rec)
# print(records.estimated_document_count())
# myquery = { "isbn": "fghj" }
# newvalues = { "$set": { "qty": 100 } }
# query={'books.'}
# x=records1.update_many(myquery, newvalues)
# records2.update_many(query, values)
# print(x.modified_count)
'''
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
                
print(id)
print(isbn)
print(title)
print(price)
print(pub_id)
print(author)
print(category)
print(quantity)
'''
# import streamlit as st


# def on_more_click(show_more, idx):
#     show_more[idx] = True


# def on_less_click(show_more, idx):
#     show_more[idx] = False


# if "show_more" not in st.session_state:
#     st.session_state["show_more"] = dict.fromkeys([1, 2, 3], False)
# show_more = st.session_state["show_more"]

# cols = st.columns(2)
# fields = ["id", "content"]

# # header
# for col, field in zip(cols, fields):
#     col.write("**" + field + "**")

# # rows
# for idx, row in zip([1, 2, 3], ["test1", "test2", "test3"]):

#     col1, col2 = st.columns(2)
#     col1.write(str(idx))
#     placeholder = col2.empty()

#     if show_more[idx]:
#         placeholder.button(
#             "less", key=str(idx) + "_", on_click=on_less_click, args=[show_more, idx]
#         )

#         # do stuff
#         st.write("This is some more stuff with a checkbox")
#         temp = st.selectbox("Select one", ["A", "B", "C"], key=idx)
#         st.write("You picked ", temp)
#         st.write("---")
#     else:
#         placeholder.button(
#             "more",
#             key=idx,
#             on_click=on_more_click,
#             args=[show_more, idx],
#             type="primary",
#         )
