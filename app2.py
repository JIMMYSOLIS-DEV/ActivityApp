import streamlit as st


st.set_page_config(page_title="Data Warehousing & Enterprise Data Management")


st.sidebar.header("Filters & Options")
selected_topic = st.sidebar.selectbox(
    "Select a Topic", 
    ["Data Warehousing", "ETL Processes", "Data Governance", "Data Modeling", "Enterprise Data Management"]
)


st.title(f"Overview of {selected_topic}")


tabs = st.tabs([selected_topic, "Additional Resources"])

with tabs[0]:
    if selected_topic == "Data Warehousing":
        st.header("What is Data Warehousing?")
        st.write("""
        Data warehousing involves the process of collecting, storing, and managing large volumes of data 
        from different sources into a central repository for analytical reporting and decision-making. 
        Data warehouses provide a unified and consistent view of data, which allows businesses to derive 
        insights for strategic planning and operational efficiency.
        """)
        
        st.expander("Learn more about Data Warehousing").write("""
        A data warehouse typically stores historical data and enables users to run complex queries and 
        generate reports. It is optimized for analytical processing, and data is typically loaded in batches. 
        Popular data warehousing tools include Amazon Redshift, Google BigQuery, and Snowflake.
        """)

    elif selected_topic == "ETL Processes":
        st.header("What are ETL Processes?")
        st.write("""
        ETL stands for Extract, Transform, and Load. It is the process of moving data from different sources 
        to a data warehouse, cleaning and transforming it into a suitable format for analysis. ETL ensures data 
        consistency, quality, and integration from multiple systems.
        """)
        
        st.expander("Learn more about ETL Processes").write("""
        ETL tools extract data from source systems, perform necessary transformations (such as data cleaning, 
        aggregation, or mapping), and then load it into the target data warehouse. Popular ETL tools include 
        Apache NiFi, Talend, and Microsoft SQL Server Integration Services (SSIS).
        """)

    elif selected_topic == "Data Governance":
        st.header("What is Data Governance?")
        st.write("""
        Data Governance refers to the management of data availability, usability, integrity, and security 
        in an organization. It ensures that data is accurate, consistent, and properly managed across its lifecycle.
        """)
        
        st.expander("Learn more about Data Governance").write("""
        Effective data governance helps organizations comply with regulatory requirements, reduce data risks, 
        and make data-driven decisions. It includes the creation of policies, data stewardship, data quality 
        controls, and metadata management practices.
        """)

    elif selected_topic == "Data Modeling":
        st.header("What is Data Modeling?")
        st.write("""
        Data Modeling involves designing the structure of data and relationships within a database or data warehouse. 
        It helps in defining how data is represented, stored, and manipulated to meet business requirements.
        """)
        
        st.expander("Learn more about Data Modeling").write("""
        Data models can be categorized into conceptual, logical, and physical models. They play a critical role 
        in structuring data for ease of access, performance, and compliance with business requirements.
        """)

    elif selected_topic == "Enterprise Data Management":
        st.header("What is Enterprise Data Management?")
        st.write("""
        Enterprise Data Management (EDM) refers to the policies, processes, and technologies used to manage 
        data across an organization to maximize its value. EDM aims to ensure the availability, accuracy, 
        security, and accessibility of data for decision-making purposes.
        """)
        
        st.expander("Learn more about Enterprise Data Management").write("""
        EDM includes practices such as data quality management, master data management, data integration, and 
        data governance. By implementing EDM, organizations can improve their data consistency, reduce 
        redundancy, and enhance decision-making capabilities.
        """)

with tabs[1]:
    st.header("Additional Resources")
    st.write("""
    - [Data Warehousing Fundamentals](https://www.example.com)
    - [ETL Best Practices](https://www.example.com)
    - [Data Governance Guide](https://www.example.com)
    - [Enterprise Data Management Overview](https://www.example.com)
    """)

    st.write("For more resources, explore related books, articles, and online courses!")

# Footer
st.markdown("---")
st.write("Made with 💻 using Streamlit")
