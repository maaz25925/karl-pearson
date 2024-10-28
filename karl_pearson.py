import pandas as pd
from math import sqrt

x = list(map(int, input("Enter X: ").split()))
y = list(map(int, input("Enter Y: ").split()))

df = pd.DataFrame({"x": x, "y": y})

n = len(x)

mean_x = sum(x) / n
mean_y = sum(y) / n

if mean_x.is_integer() and mean_y.is_integer():

    direct_method = True

    for i in range(n):
        if x[i] > 20 or y[i] > 20:
            direct_method = False
            break

    if direct_method:
        print("Direct Method\n")

        df["x²"] = df["x"] ** 2
        df["y²"] = df["y"] ** 2
        df["xy"] = df["x"] * df["y"]

        print(df.to_string(index=False), "\n")

        # Print mean and summation values
        print(f"x̄ = {sum(x)} / {n} = {int(mean_x)}")
        print(f"ȳ = {sum(y)} / {n} = {int(mean_y)}")

        print(f"Σ(x²): {int(df['x²'].sum())}")
        print(f"Σ(y²): {int(df['y²'].sum())}")
        print(f"Σ(xy): {int(df['xy'].sum())}\n")

        covariance = (df["xy"].sum() / n) - ((mean_x) * (mean_y))
        sigma_x = sqrt((df["x²"].sum() / n) - (mean_x ** 2))
        sigma_y = sqrt((df["y²"].sum() / n) - (mean_y ** 2))
        r = covariance / (sigma_x * sigma_y) if sigma_x != 0 and sigma_y != 0 else None

        print("cov(x, y) = (Σ(xy) / n) - (x̄ * ȳ)")
        print(f"cov(x, y) = ({df['xy'].sum()} / {n}) - ({mean_x} * {mean_y})")
        print(f"cov(x, y) = {covariance}\n")

        print("σx = √(Σ(x²) / n)")
        print(f"σx = √({df['x²'].sum()} / {n})")
        print(f"σx = {sigma_x}\n")

        print("σy = √(Σ(y²) / n)")
        print(f"σy = √({df['y²'].sum()} / {n})")
        print(f"σy = {sigma_y}\n")

        print("r = cov(x, y) / (σx * σy)")
        print(f"r = {covariance} / ({sigma_x} * {sigma_y})")
        print(f"r = {r}")
    else:
        print("Deviation from Mean Method\n")

        df["x-x̄"] = df["x"] - mean_x
        df["y-ȳ"] = df["y"] - mean_y
        df["(x-x̄)²"] = df["x-x̄"] ** 2
        df["(y-ȳ)²"] = df["y-ȳ"] ** 2
        df["(x-x̄)(y-ȳ)"] = df["x-x̄"] * df["y-ȳ"]

        print(df, "\n")

        # Print mean and summation values
        print(f"x̄ = {sum(x)} / {n} = {int(mean_x)}")
        print(f"ȳ = {sum(y)} / {n} = {int(mean_y)}")

        print(f"Σ(x-x̄): {int(df["x-x̄"].sum())}")
        print(f"Σ(y-ȳ): {int(df["y-ȳ"].sum())}")
        print(f"Σ(x-x̄²): {int(df["(x-x̄)²"].sum())}")
        print(f"Σ(y-ȳ²): {int(df["(y-ȳ)²"].sum())}")
        print(f"Σ(x-x̄)(y-ȳ): {int(df["(x-x̄)(y-ȳ)"].sum())}\n")

        covariance = df["(x-x̄)(y-ȳ)"].sum() / n
        sigma_x = sqrt(df["(x-x̄)²"].sum() / n)
        sigma_y = sqrt(df["(y-ȳ)²"].sum() / n)
        r = covariance / (sigma_x * sigma_y) if sigma_x != 0 and sigma_y != 0 else None

        print("cov(x, y) = Σ(x-x̄)(y-ȳ) / n")
        print(f"cov(x, y) = {df['(x-x̄)(y-ȳ)'].sum()} / {n}")
        print(f"cov(x, y) = {covariance}\n")

        print("σx = √(Σ(x-x̄²) / n)")
        print(f"σx = √({df['(x-x̄)²'].sum()} / {n})")
        print(f"σx = {sigma_x}\n")

        print("σy = √(Σ(y-ȳ²) / n)")
        print(f"σy = √({df['(y-ȳ)²'].sum()} / {n})")
        print(f"σy = {sigma_y}\n")

        print("r = cov(x, y) / (σx * σy)")
        print(f"r = {covariance} / ({sigma_x} * {sigma_y})")
        print(f"r = {r}")
else:
    print("Assumed Mean Method\n")
    
    a = round(mean_x)
    b = round(mean_y)

    df["dx=(x-A)"] = df["x"] - a
    df["dy=(y-B)"] = df["y"] - b
    df["dx²"] = df["dx=(x-A)"] ** 2
    df["dy²"] = df["dy=(y-B)"] ** 2
    df["dx*dy"] = df["dx=(x-A)"] * df["dy=(y-B)"]

    print(df, "\n")

    print(f"x̄ = {sum(x)} / {n} = {mean_x} (A = {a})")
    print(f"ȳ = {sum(y)} / {n} = {mean_y} (B = {b})\n")

    print(f"Σ(dx): {df['dx=(x-A)'].sum()}")
    print(f"Σ(dy): {df['dy=(y-B)'].sum()}")
    print(f"Σ(dx²): {df['dx²'].sum()}")
    print(f"Σ(dy²): {df['dy²'].sum()}")
    print(f"Σ(dx*dy): {df['dx*dy'].sum()}\n")

    covariance = (df["dx*dy"].sum() / n) - ((df["dx=(x-A)"].sum() / n) * (df["dy=(y-B)"].sum() / n))
    sigma_x = sqrt((df["dx²"].sum() / n) - (df["dx=(x-A)"].sum() / n) ** 2)
    sigma_y = sqrt((df["dy²"].sum() / n) - (df["dy=(y-B)"].sum() / n) ** 2)
    r = covariance / (sigma_x * sigma_y) if sigma_x != 0 and sigma_y != 0 else None

    print("cov(x, y) = (Σ(dx * dy) / n) - (Σ(dx) / n) * (Σ(dy) / n)")
    print(f"cov(x, y) = ({df["dx*dy"].sum()} / {n}) - ({df['dx=(x-A)'].sum()} / {n}) * ({df['dy=(y-B)'].sum()} / {n})")
    print(f"cov(x, y) = {covariance}\n")

    print("σx = √((Σ(dx²) / n) - (Σ(dx) / n)²)")
    print(f"σx = √(({df['dx²'].sum()} / {n}) - ({df['dx=(x-A)'].sum()} / {n})²)")
    print(f"σx = {sigma_x}\n")

    print("σy = √((Σ(dy²) / n) - (Σ(dy) / n)²)")
    print(f"σy = √(({df['dy²'].sum()} / {n}) - ({df['dy=(y-B)'].sum()} / {n})²)")
    print(f"σy = {sigma_y}\n")

    print("r = cov(x, y) / (σx * σy)")
    print(f"r = {covariance} / ({sigma_x} * {sigma_y})")
    print(f"r = {r}")
