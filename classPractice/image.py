def my_index:
    ret = ''
    for i in range(1, 11):
        ret = ret + '<tr><td><img src="image/{}.jpg" width="200"/></td></tr>'.format(i)
    return ret
html = '''

<html>
    <head>
        <meta charset="utf-8">
        <title>
            Picture page
        </title>
    </head>
    <body>
        <table>
            {}
        </table>
    </body>
</html>
'''.format(my_index())
print(html)