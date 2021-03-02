text = '''
<html>
    <body>
        <h1>Heading</h1>
    </body>
</html>
'''

print(text)

file = open("sample.html","w")
file.write(text)
file.close()