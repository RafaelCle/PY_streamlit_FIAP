import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns



# Função para gerar visualizações

def generate_visualization(visualization_type, variable):
    if visualization_type == "Histograma":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(filtered_data[variable], kde=True, ax=ax)
        ax.set_title(f'Histograma de {variable}')
        st.pyplot(fig)

    elif visualization_type == "Boxplot":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(filtered_data[variable], orient='h', ax=ax)
        ax.set_title(f'Boxplot de {variable}')
        st.pyplot(fig)

    elif visualization_type == "Pie Chart":
        fig, ax = plt.subplots(figsize=(10, 6))
        pie_data = filtered_data[variable].value_counts().reset_index()
        pie_data.columns = [variable, 'count']
        ax.pie(pie_data['count'], labels=pie_data[variable], autopct='%.1f%%')
        ax.set_title(f'Pie Chart de {variable}')
        st.pyplot(fig)

    elif visualization_type == "Barplot":
        fig, ax = plt.subplots(figsize=(10, 6))
        bar_data = filtered_data[variable].value_counts().reset_index()
        bar_data.columns = [variable, 'count']
        sns.barplot(x='count', y=variable, data=bar_data, ax=ax)
        ax.set_title(f'Barplot de {variable}')
        ax.set_xlabel('Count')
        ax.set_ylabel(variable)
        st.pyplot(fig)



# Carregar o dataset

data = pd.read_csv('https://raw.githubusercontent.com/lcbjrrr/quantai/refs/heads/main/activities/travel%20-%20insurance.csv')

 
# Filtros interativos
st.sidebar.title("Filtros")

 

Agency_filter = st.sidebar.multiselect("Agency", data.Agency.unique(), default=data.Agency.unique())
Agency_type_filter = st.sidebar.multiselect("Agency Type", data['Agency Type'].unique(), default=data['Agency Type'].unique())
Claim_filter = st.sidebar.multiselect("Claim", data['Claim'].unique(), default=data['Claim'].unique())
Destination_filter = st.sidebar.multiselect("Destination", data['Destination'].unique(), default=data['Destination'].unique())
Distribution_Channel_filter = st.sidebar.multiselect("Distribution Channel", data['Distribution Channel'].unique(), default=data['Distribution Channel'].unique())
Gender_filter = st.sidebar.multiselect("Gender", data['Gender'].unique(), default=data['Gender'].unique())
Product_Name_filter = st.sidebar.multiselect("Product Name", data['Product Name'].unique(), default=data['Product Name'].unique())

duration_filter = st.sidebar.slider("Duration", int(data['Duration'].min()), int(data['Duration'].max()), (int(data['Duration'].min()), int(data['Duration'].max())))
net_sales_filter = st.sidebar.slider("Net Sales", int(data['Net Sales'].min()), int(data['Net Sales'].max()), (int(data['Net Sales'].min()), int(data['Net Sales'].max())))
commision_filter = st.sidebar.slider("Commision (in value)", int(data['Commision (in value)'].min()), int(data['Commision (in value)'].max()), (int(data['Commision (in value)'].min()), int(data['Commision (in value)'].max())))
age_filter = st.sidebar.slider("Age", int(data['Age'].min()), int(data['Age'].max()), (int(data['Age'].min()), int(data['Age'].max())))

 

filtered_data = data[(data['Duration'] >= duration_filter[0]) & (data['Duration'] <= duration_filter[1]) &
                     (data['Net Sales'] >= net_sales_filter[0]) & (data['Net Sales'] <= net_sales_filter[1]) &
                     (data['Commision (in value)'] >= commision_filter[0]) & (data['Commision (in value)'] <= commision_filter[1]) &
                     (data['Age'] >= age_filter[0]) & (data['Age'] <= age_filter[1]) &
                     (data['Agency'].isin(Agency_filter)) &
                     (data['Agency Type'].isin(Agency_type_filter)) &
                     (data['Claim'].isin(Claim_filter)) &
                     (data['Destination'].isin(Destination_filter)) &
                     (data['Distribution Channel'].isin(Distribution_Channel_filter)) &
                     (data['Gender'].isin(Gender_filter)) &
                     (data['Product Name'].isin(Product_Name_filter))
                     ]

 

# Título do dashboard
st.title("Análise Exploratória de Dados - Travel Insurance")


# Exibir o dataframe
st.subheader("Dados do Travel Insurance")
st.dataframe(filtered_data)


# Medidas resumo numéricas
st.subheader("Medidas Resumo Numéricas")
st.write(filtered_data.describe().round(2))

# Medidas resumo numéricas
st.subheader("Medidas Resumo Numéricas")

# Lista suspensa para escolher o tipo d visualização
categorica = ['Agency','Agency Type','Claim','Destination', 'Distribution Channel', 'Gender', 'Product Name']
numerica = ['Net Sales','Duration','Commision (in value)','Age']

dtype = st.selectbox("Selecione o tipo de variável:", ['Categórica', 'Numérica'])


if dtype == 'Categórica':  
    visualization_type = st.selectbox("Selecione o Tipo de Visualização", ["Pie Chart", "Barplot"])
    variable = st.selectbox("Selecione a Variável",  categorica)
    generate_visualization(visualization_type, variable)

   

else:
    visualization_type = st.selectbox("Selecione o Tipo de Visualização", ["Histograma", "Boxplot"])
    variable = st.selectbox("Selecione a Variável",  numerica)
    generate_visualization(visualization_type, variable)
