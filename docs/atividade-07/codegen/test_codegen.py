import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("button", name="Criar Conta").click()
    page.get_by_role("textbox", name="Seu nome").click()
    page.get_by_role("textbox", name="Seu nome").fill("Gabrieli Morales")
    page.get_by_role("textbox", name="novo@teste.com").click()
    page.get_by_role("textbox", name="novo@teste.com").fill("gabrielimoralestaborda@gmail.com")
    page.get_by_role("textbox", name="Min. 3 caracteres").click()
    page.get_by_role("textbox", name="Min. 3 caracteres").fill("1234")
    page.get_by_role("button", name="Registrar").click()
    page.get_by_text("Olá, Gabrieli").click()
    page.get_by_title("Sair").click()
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("gabrielimoralestaborda@gmail.com")
    page.get_by_role("textbox", name="teste@teste.com").press("Tab")
    page.get_by_role("textbox", name="Sua senha secreta").fill("1234")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
