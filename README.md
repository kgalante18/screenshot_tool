# screenshot_tool

This tool enables users to capture full-page screenshots of web pages using the Selenium package. By automating the process, it saves time and effort compared to manual methods

To use the screenshot tool, first create an instance of the Screenshot_Tool class by specifying the URL of the webpage you want to capture. Then, call the scroll_to_bottom method to scroll to the bottom of the page and ensure that the entire page is loaded. Finally, call the full_page_screenshot method to capture a screenshot of the entire webpage. 

Here is an example:

execute_screenshot_tool = Screenshot_Tool(url= '')
execute_screenshot_tool.scroll_to_bottom()
execute_screenshot_tool.full_page_screenshot()
