import pyautogui
import pyperclip
import pandas as pd

def main():
    df = pd.read_csv("Artikel_Add.csv")
    for i, row in df.iterrows():
        pyautogui.click(200, 60)
        pyperclip.copy(row["Artikelnummer"])
        pyautogui.hotkey("ctrl", "v")
        
        pyautogui.click(200,120)
        pyperclip.copy(row["Name"])
        pyautogui.hotkey("ctrl", "v")
        
        pyautogui.click(200,170)
        pyperclip.copy(row["Hersteller"])
        pyautogui.hotkey("ctrl", "v")
        
        pyautogui.click(200,220)
        pyperclip.copy(row["Preis"])
        pyautogui.hotkey("ctrl", "v")
        
        pyautogui.click(200, 270)
        pyautogui.click(1000, 600)
        
        
    
    
    
if __name__ == "__main__":
    main()