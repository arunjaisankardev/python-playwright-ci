from playwright.sync_api import Page, expect


def test_home_page_title(page: Page):
    page.goto("/")
    expect(page).to_have_title("Playwright CI Demo")


def test_button_click_updates_text(page: Page):
    page.goto("/")
    page.get_by_role("button", name="Click me").click()
    result = page.locator("#result")
    expect(result).to_be_visible()
    expect(result).to_have_text("Button clicked!")


def test_logo_image_is_visible(page: Page):
    page.goto("/")
    logo = page.locator("img#logo")
    expect(logo).to_be_visible()
    natural_width = page.evaluate(
        "() => document.getElementById('logo').naturalWidth"
    )
    assert natural_width > 0
