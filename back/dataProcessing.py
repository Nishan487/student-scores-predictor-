import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def clean_score(filepath):
    df=pd.read_csv(filepath)
    df=df.dropna()
    return df

def figure(df):
    df.plot(x='Hours', y='Scores', style='o')
    plt.title('Hours vs Percentage')
    plt.xlabel('Hours Studied')
    plt.ylabel('Percentage Score')
    plt.savefig("static/plot.png")
    plt.close()

def train_score(df):
    X = df[['Hours']]
    y= df['Scores']
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")
    print(f"Root Mean Squared Error: {rmse}")
    print(f"R^2 Score: {r2}")
    return model

def predict_score(model, hours):
    input_df = pd.DataFrame({'Hours':[hours]})
    predicted_score = model.predict(input_df)
    return predicted_score[0]
    
def main(filepath,hours):
    df = clean_score(filepath)
    
    df=pd.DataFrame(df)
    figure(df)
    model = train_score(df)
    predicted_score = predict_score(model, hours)
    print(f"Predicted score for studying {hours} hours: {predicted_score}")
    return predicted_score
    

    
    