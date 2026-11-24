import pandas as pd
import numpy as np

EXCEL_FILE = "data/vostokhome_recsys_project_data.xlsx"

def run_simulation():
    xls = pd.ExcelFile(EXCEL_FILE)
    print("Загружены листы:", xls.sheet_names)

    products = pd.read_excel(xls, "02_Products_200")
    u_before = pd.read_excel(xls, "06_UserPref_Before")
    u_after = pd.read_excel(xls, "07_UserPref_After")
    g_cat = pd.read_excel(xls, "10_GroupCat_After")
    i_pref = pd.read_excel(xls, "13_ItemPref_200x12")
    links = pd.read_excel(xls, "11_ItemLinks_Sparse")

    # Пример пересчёта для USR-01 после покупки PRD-085
    u1_old = u_before.loc[u_before["ID_Пользователя"] == "USR-01", "PRF-04"].values[0]
    i85_p4 = i_pref.loc[i_pref["ID_Товара"] == "PRD-085", "PRF-04"].values[0]
    w_sum = 0.03 + 0.10 + 0.15  # VIEW + CART_ADD + PURCHASE
    u1_new = np.clip(u1_old * np.exp(-0.01 * 0) + 0.50 * w_sum * i85_p4, -1.0, 1.0)
    print(f"USR-01 PRF-04: до={u1_old:.2f}, расчёт={u1_new:.2f}, в таблице после={u_after.loc[0, 'PRF-04']:.2f}")

    # Проверка фильтрации нулевых остатков
    zero_stock = products[products["Остаток"] == 0]["ID_Товара"].tolist()
    print("Исключены из рекомендаций (stock=0):", zero_stock)

if __name__ == "__main__":
    run_simulation()
