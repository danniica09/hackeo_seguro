import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import linearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squeared_error,r2_score
from captura import CapturaDatos



class PrepareData:

    def __init__(self):
       self.listReturned = CapturaDatos()
       self.listData = []


    def prepareJson(self):
        self.listReturned.Captura()
        self.listData = self.listReturned.limpieza()


    def pandasDataPrepare(self):
        df = pd.DataFrame(self.listData,columns=["year","quarter","provider","income","amountSMS"])
        df['year'] = pd.to_datetime(df['year'])
        df['quarter'] = df['quarter'].astype('category').cat.codes
        df['provider'] = df['provider'].astype('category').cat.codes

        x = df["year","quarter","provider","amountSMS"]
        y = df["income"]

        x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.2,random_state=42)

        model = LineaRegression()
        model.fit(x_train,y_train)

        y_pred = model.predict(x_test)

        nse = mean_squeared_error(y_test, y_pred)
        r2 = r2_score(y_test,y_pred)

        print(f"mean error:{nse}")
        print(f"R-squared error:{r2}")

        plt.scatter(y_test, y_pred)
        plt.xlabel("% real income")
        plt.ylabel("income prediction")
        plt.show()

prueba = PrepareData()
prueba.prepareJson()
prueba.pandasDataPrepare()
