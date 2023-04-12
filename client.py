import streamlit as st
from streamlit_option_menu import option_menu
# from streamlit.script_runner import SessionState

from pymongo import MongoClient
import pandas as pd

client=MongoClient("mongodb+srv://sarvesh:sarvesh@cluster0.fi6cwh7.mongodb.net/?retryWrites=true&w=majority")
db=client.get_database('database')
records1=db.lib_1
records2=db.lib_2
st.set_page_config(page_title="Client",layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# st.set_theme('dark')


# st.write(records1.find({'user_id':101}))
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# def remote_css(url):
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

# def icon(icon_name):
#     st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

# local_css("style.css")
# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# inp=st.text_input("User ID")
# passw=st.text_input("Password",type="password")
# c1,c2,c3=st.columns([2,1,2])
# with c2:
#     enter=st.button("Enter")
# if enter:
#     # opt_main=
#     try:
#         quer = {"user_id": int(inp)}
#         user_document = records2.find_one(quer)
#         password = user_document["pass"]
#         if passw==password:
#             with c2:
#                 st.subheader("Logged in as "+user_document["user_name"])
#                 l=1
#             options=["--Choose--","Search", "Books to be returned", "Bookmarks","Reset"]
            # opt = option_menu(
            #                 menu_title=None,  # required
            #                 options=["Search", "Books to be returned", "Bookmarks","Reset"],  # required
            #                 icons=["search", "book","bookmarks","123"],  # optional
            #                 menu_icon="cast",  # optional
            #                 default_index=1,  # optional
            #                 orientation="vertical",
            #             )
#             opt=st.sidebar.selectbox("Menu",options)
#             # if st.button("Choose"):
#             # opt = st.radio(
#             #     "Choose",
#             #     ('Search', 'Books to be returned'))
#             if opt=='Search':
#                 # icon("search")
#                 selected = st.text_input("Search")
#                 button_clicked = st.button("OK")
#                 if button_clicked:
#                     pass
#             elif opt=="Bookmarks":
#                 st.title("ok")

#             elif opt=='Books to be returned':
#                 # print("kk")
#                 # inp=st.text_input("Your user ID")
#                 # if st.button("OK"):
#                     try:
#                         query = {"user_id": int(inp)}
#                         pipeline1 = [
#                     {"$match": query},
#                     {"$project": {"values": {"$map": {"input": "$books", "as": "b", "in": "$$b.isbn"}}}}]
#                         result1 = list(records2.aggregate(pipeline1))[0]  
#                         isbn_values = result1["values"]

#                         pipeline2 = [
#                     {"$match": query},
#                     {"$project": {"values": {"$map": {"input": "$books", "as": "b", "in": "$$b.title"}}}}]
#                         result2 = list(records2.aggregate(pipeline2))[0]  
#                         title_values = result2["values"]
#                         data={
#                             'ISBN':isbn_values,
#                             'Title':title_values
#                         }
#                         df = pd.DataFrame(data)
#                         df.index += 1
#                         df.index.name = 'Row'
#                         st.dataframe(df)
#                     except Exception:
#                         st.warning("Try using valid User ID")
#         else:
#             st.error("Incorrect login credentials")
#     except TypeError:
#         st.warning("Incorrect username/password")
#####copy1

# options = ["--Choose--", "Search", "Books to be returned", "Bookmarks", "Reset"]

# # Define the sidebar
# st.sidebar.title("Menu")
# selected_option = st.sidebar.selectbox("", options)

# # Define the session state
# if "state" not in st.session_state:
#     st.session_state.state = {
#         "user_id": None,
#         "password": None,
#         "logged_in": False,
#         "selected_option": None,
#     }

# # Define the form to get the user's credentials
# if not st.session_state.state["logged_in"]:
#     user_id = st.text_input("User ID")
#     password = st.text_input("Password", type="password")
#     if st.button("Login"):
#         query = {"user_id": int(user_id)}
#         user_document = records2.find_one(query)
#         if user_document is not None and password == user_document["pass"]:
#             st.success("Logged in as " + user_document["user_name"])
#             st.session_state.state["user_id"] = user_id
#             st.session_state.state["password"] = password
#             st.session_state.state["logged_in"] = True
#         else:
#             st.error("Incorrect user ID or password")

# # Define the functionality based on the selected option
# if st.session_state.state["logged_in"] and selected_option != "--Choose--":
#     if selected_option == "Search":
#         selected = st.text_input("Search")
#         if st.button("OK"):
#             pass
#     elif selected_option == "Bookmarks":
#         st.title("OK")
#     elif selected_option == "Books to be returned":
#         query = {"user_id": int(st.session_state.state["user_id"])}
#         pipeline1 = [
#             {"$match": query},
#             {"$project": {"values": {"$map": {"input": "$books", "as": "b", "in": "$$b.isbn"}}}},
#         ]
#         result1 = list(records2.aggregate(pipeline1))[0]
#         isbn_values = result1["values"]
#         pipeline2 = [
#             {"$match": query},
#             {"$project": {"values": {"$map": {"input": "$books", "as": "b", "in": "$$b.title"}}}},
#         ]
#         result2 = list(records2.aggregate(pipeline2))[0]
#         title_values = result2["values"]
#         data = {"ISBN": isbn_values, "Title": title_values}
#         df = pd.DataFrame(data)
#         df.index += 1
#         df.index.name = "Row"
#         st.dataframe(df)
#     elif selected_option == "Reset":
#         st.session_state.state = {
#             "user_id": None,
#             "password": None,
#             "logged_in": False,
#             "selected_option": None,
#         }
#         st.success("Reset successful. Please login again.")     
options = ["--Choose--", "Search", "Books to be returned", "Bookmarks", "Reset", "Reset password"]

if "state" not in st.session_state:
    st.session_state.state = {
        "user_id": None,
        "password": None,
        "logged_in": False,
        "selected_option": None,
    }

# Define the form to get the user's credentials
if not st.session_state.state["logged_in"]:
    st.title("Login")
    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")
    c1,c2,c3=st.columns([2,1,2])
    with c2:
        login=st.button("Login")
    if login:
        query = {"user_id": int(user_id)}
        user_document = records2.find_one(query)
        if user_document is not None and password == user_document["pass"]:
            # c1,c2,c3=st.columns([0.7,1,2])
            # with c2:
            st.success("Logged in as " + user_document["user_name"])
            st.session_state.state["user_id"] = user_id
            st.session_state.state["password"] = password
            st.session_state.state["logged_in"] = True
        else:
            st.error("Incorrect user ID or password")

# Define the functionality based on the selected option
if st.session_state.state["logged_in"]:
    st.title("Options")
    selected_option =  option_menu(
                            menu_title=None,  # required
                            options=["Search", "Books to be returned","Reset Password", "Logout"],  # required
                            icons=["search", "book","123","door-closed-fill"],  # optional
                            menu_icon="cast",  # optional
                            default_index=0,  # optional
                            orientation="horizontal",
                        )
    st.session_state.state["selected_option"] = selected_option
    if selected_option == "Search":
        selected = st.text_input("Search")
        c1,c2,c3=st.columns([2,1,2])
        with c2:
            search=st.button("Search")
        if search:
            id=[]
            isbn=[]
            title=[]
            price=[]
            pub_id=[]
            author=[]
            category=[]
            quantity=[]
            for i in records1.find():
                if selected in i["title"]:
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
                "Quantity": quantity,
            }

            df = pd.DataFrame(data)
            df.index += 1
            df.index.name = 'Row'
            c1,c2,c3=st.columns([0.7,1,1])
            with c2:
                st.dataframe(df)
                
    elif selected_option == "Bookmarks":
        st.write('''<h3>Bookmarks</h3>''',unsafe_allow_html=True)
    elif selected_option == "Books to be returned":
        st.write('''<h3>Books to be returned</h3>''',unsafe_allow_html=True)
        query = {"user_id": int(st.session_state.state["user_id"])}
        pipeline1 = [
            {"$match": query},
            {"$project": {"values": {"$map": {"input": "$books", "as": "b", "in": "$$b.isbn"}}}},
        ]
        result1 = list(records2.aggregate(pipeline1))[0]
        isbn_values = result1["values"]
        pipeline2 = [
            {"$match": query},
            {"$project": {"values": {"$map": {"input": "$books", "as": "b", "in": "$$b.title"}}}},
        ]
        c1,c2,c3=st.columns([2,1,2])
        with c2:
            result2 = list(records2.aggregate(pipeline2))[0]
            title_values = result2["values"]
            data = {"ISBN": isbn_values, "Title": title_values}
            df = pd.DataFrame(data)
            df.index += 1
            df.index.name = "Row"
            st.dataframe(df)
    elif selected_option == "Reset Password":
        st.write('''<h3>Reset Password</h3>''',unsafe_allow_html=True)
        curr=st.text_input("Current Password")
        new=st.text_input("New Password")
        c1,c2,c3=st.columns([2,1,2])
        with c2:
            reset=st.button("Reset")
        if reset:
            if curr==st.session_state.state["password"]:
                query = {"user_id": int(st.session_state.state["user_id"])}
                update = {"$set": {"pass": new}}
                result = records2.update_one(query, update)
                if result.modified_count==1:
    
                        st.success("Updated Successfully!")
            else:
                    st.error("Invalid current password")
    elif selected_option == "Logout":
        st.session_state.state = {
            "user_id": None,
            "password": None,
            "logged_in": False,
            "selected_option": None,
        }
        c1,c2,c3=st.columns([1,1,1])
        with c2:
            st.write('''<h3>Successfully logged out</h3>''',unsafe_allow_html=True)
        # st.session_state.state["selected_option"] = "--Choose--" # reset selected option