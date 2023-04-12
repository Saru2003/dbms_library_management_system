# import pandas as pd
# import streamlit as st

# # create a dataframe with a boolean column
# df = pd.DataFrame({"A": [True, False, True, False]})

# # show the data editor with checkboxes
# selected_rows = st.experimental_data_editor(df)

# # access the selected rows
# if st.button("g"):
#     if selected_rows:
#         st.write("Selected rows:", selected_rows)
#     else:
#         st.write("No rows selected")

import pandas as pd
import streamlit as st

# create a dataframe with a boolean column
df = pd.DataFrame({"Selected": [True]*4})

# show the data editor with checkboxes
selected_rows = st.experimental_data_editor(df)

# access the selected rows
if st.button("g"):
    if isinstance(selected_rows, pd.DataFrame):
        selected_rows = selected_rows.index[selected_rows["Selected"].astype(bool)].tolist()
        st.write("Selected rows:", selected_rows)
    else:
        st.write("No rows selected")
