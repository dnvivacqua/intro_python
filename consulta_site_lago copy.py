import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://yodelportal.com/buntzen-lake/Half-Day-Pass")
    page.get_by_role("link", name="Profile").click()
    page.locator("#txtPhonenumber").click()
    page.locator("#txtPhonenumber").fill("7788825456")
    page.get_by_role("link", name="Next").click()
 
    page.get_by_role("link", name="Done").click()
    page.locator("#cardInstruction_12197").get_by_text("Available").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
