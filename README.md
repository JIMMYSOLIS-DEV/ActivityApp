Code
![Screenshot 2025-05-06 024503](https://github.com/user-attachments/assets/b0b57995-b38a-4ef7-9445-ba3e0cd3852e)
Output
![Screenshot 2025-05-06 024750](https://github.com/user-attachments/assets/2d4beded-b16c-40a7-9fa1-5a806bed4c05)
Explanation
You can upload a CSV file using st.file_uploader, then load it with pandas to turn it into a table. After that, you can display the table using st.dataframe. If you want, you can add a checkbox with st.checkbox to let users hide or show the data. You can also let users filter the data by a column using st.selectbox. Just make sure the CSV file has at least 5 columns before you start.
