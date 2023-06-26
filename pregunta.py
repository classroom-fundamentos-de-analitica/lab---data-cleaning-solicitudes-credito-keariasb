"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    SC = pd.read_csv("solicitudes_credito.csv", sep=";")
    SC.dropna(axis = 0, inplace = True)
    SC.drop_duplicates(inplace = True)

    SC.fecha_de_beneficio = pd.to_datetime(SC.fecha_de_beneficio,infer_datetime_format=True,errors='ignore',dayfirst=True)
    SC.fecha_de_beneficio = SC.fecha_de_beneficio.dt.strftime("%Y/%m/%d")

    SC=SC.drop(['Unnamed: 0'], axis=1)
    SC[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]]=SC[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]].apply(lambda x: x.astype(str).str.lower())
    SC=SC.replace(to_replace="(_)|(-)",value=" ",regex=True)    
    SC=SC.replace(to_replace="[,$]|(\.00$)",value="",regex=True)

    SC.monto_del_credito = SC.monto_del_credito.astype("int")

    SC.comuna_ciudadano = SC.comuna_ciudadano.astype("float")

    SC.drop_duplicates(inplace = True)

    return SC
