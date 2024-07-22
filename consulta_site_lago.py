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
    page.get_by_placeholder("Enter email").click()
    page.get_by_placeholder("Enter email").fill("dan.nascim@gmail.com")
    page.get_by_placeholder("Enter email").press("Tab")
    page.get_by_text("First Name *").press("Tab")
    page.get_by_placeholder("Enter First Name").fill("Daniel")
    page.get_by_placeholder("Enter First Name").press("Tab")
    page.get_by_text("Last Name *").press("Tab")
    page.get_by_placeholder("Enter Last Name").fill("Vivacqua")
    page.get_by_role("link", name="Next").click()
    page.get_by_label("Please enter verification").click()
    page.get_by_label("Please enter verification").fill("5")
    page.get_by_label("Digit 2").fill("8")
    page.get_by_label("Digit 3").fill("8")
    page.get_by_label("Digit 4").fill("3")
    page.get_by_role("link", name="Done").click()
    page.locator("#cardInstruction_12197").get_by_text("Available").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
