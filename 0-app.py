import justpy as jp

def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp, text='Analysis of Course Reviews', classes='text-h2 text-center q-pa-md')
    p1=jp.QDiv(a=wp, text='These graphs represent course review analysis', 
    classes='text-h4 text-center q-pa-md')

    return wp

jp.justpy(app)