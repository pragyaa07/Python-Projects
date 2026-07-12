import pandas as pd
import matplotlib.pyplot as plt


def loss_function(m, b, data):
    error=0
    for i in range(len(data)):
        x= data.iloc[i].sqft_living
        y= data.iloc[i].price
        error += (y- (m*x + b))**2
    return error/len(data)

def grad_descent(m, b, data, L):
    m_grad=0
    b_grad=0
    n= len(data)

    for i in range(len(data)):
        x= data.iloc[i].sqft_living
        y= data.iloc[i].price

        m_grad+= -(2/n) *x *(y- (m*x + b))
        b_grad+= -(2/n) * (y- (m*x + b))
    
    M= m-L*m_grad
    B= b-L*b_grad
    return M, B

def main():
    df= pd.read_csv(".\Linear Regression\housing.csv")
    df= df.head(500)
    df["sqft_living"] /= 1000
    df["price"] /= 100000

    m=0 
    b=0
    L=0.001
    iterate= 500

    for i in range(iterate):
        m, b= grad_descent(m, b, df, L)

        if i % 50 == 0:
            loss = loss_function(m, b, df)
            print(f"Iteration {i}: Loss = {loss:.4f}")

    print(f"m = {m:.4f}, b = {b:.4f}")
    df = df.sort_values("sqft_living")
    plt.scatter(df["sqft_living"], df["price"], color="black") 
    plt.plot(df.sqft_living, m * df.sqft_living + b, color="red")

    plt.xlabel("Living Area (1000 sqft)")
    plt.ylabel("Price (Lakhs)")
    plt.show()

if __name__ == "__main__":
    main()




