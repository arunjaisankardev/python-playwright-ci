# from playwright.sync_api import Page, expect


# def test_demo_intentional_fail(page: Page):
#     """This test intentionally fails to demo CI blocking merge."""
#     page.goto("/")
#     # Expect title to contain "FAIL" - but real title is "Playwright CI Demo"
#     expect(page).to_have_title("This page is broken - FAIL")


# def test_broken_button(page: Page):
#     """Button click fails because we will change the text."""
#     page.goto("/")
#     page.get_by_role("button", name="Click me").click()
#     # Expect wrong text
#     expect(page.locator("#result")).to_have_text("Broken button!")
