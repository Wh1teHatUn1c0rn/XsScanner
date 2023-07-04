import requests
from bs4 import BeautifulSoup


def unicorn_crew_scan(url):
    # Send a get and post request to the URL
    response = requests.get(url)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all input fields in the HTML form
    form_fields = soup.find_all('input')

    # Store potential vulnerabilities
    vulnerabilities = []

    # Iterate over each input field and inject a malicious payload
    for field in form_fields:
        # Create a payload
        payload = "<script>alert('XSS vulnerability found!');</script>"

        # Replace the field value with a payload
        field['value'] = payload

        # Submit the modified form
        response = requests.post(url, data=soup.form.attrs)

        # Check if the payload appears in the response
        if payload in response.text:
            vulnerabilities.append({
                'field_name': field.get('name'),
                'payload': payload
            })
    # Print the results
    if vulnerabilities:
        print("Potential vulners found: ")
        for vuln in vulnerabilities:
            print("Field Name:", vuln['field_name'])
            print("Payload:", vuln['payload'])
            print("-----------------")
        else:
            print("No vulnerabilities found")