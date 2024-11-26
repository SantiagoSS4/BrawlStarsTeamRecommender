import pandas as pd

class DataProcessor:
    def __init__(self, archivo_csv, roles_por_mapa):
        self.archivo_csv = archivo_csv
        self.roles_por_mapa = roles_por_mapa
        self.df_inicial = pd.read_csv(archivo_csv)

    def filtrar_y_categorizar_por_mapa(self, mapa, columnas_a_categorizar):
        if mapa not in self.roles_por_mapa:
            raise ValueError(f"El mapa '{mapa}' no está definido en la configuración de roles.")
        
        roles_necesarios = self.roles_por_mapa[mapa]
        df_filtrado = self.df_inicial[self.df_inicial["Rol"].isin(roles_necesarios)]
        df_categorizado = df_filtrado.copy()
        
        for columna in columnas_a_categorizar:
            def categorizar_por_rol(rol):
                rol_df = df_filtrado[df_filtrado["Rol"] == rol]
                bajo_limite = rol_df[columna].quantile(0.33)
                medio_limite = rol_df[columna].quantile(0.66)

                def categorizar(valor):
                    if valor <= bajo_limite:
                        return 'bajo'
                    elif valor <= medio_limite:
                        return 'medio'
                    else:
                        return 'alto'

                return rol_df[columna].apply(categorizar)

            for rol in roles_necesarios:
                df_categorizado.loc[df_categorizado["Rol"] == rol, columna] = categorizar_por_rol(rol)

        return df_categorizado
