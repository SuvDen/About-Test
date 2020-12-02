import horoscope

def generate_head(title):
    head = '<title>' + title + '</title>'
    head += '<meta charset="utf-8">'
    return '<head>' + head + '</head>'

def generation_body(header):
    body = '<h1>' + header + '</h1>'
    image = '<img src="about.png" alt="">'
    body += image
    return '<body>' + body

def generate_numeration(subtitle, every_list: list):
    text = '<h2>' + subtitle + '</h2>'
    for l in every_list:
        text += '<p>' + '- ' + str(l) + '</p>'
    return text

def generate_link(text_link):
    trait = '<hr/>' + '&nbsp;'
    link = trait + '<a href="index.html">' + text_link + '</a>' + '</body>'
    return link

def save_about():
    head = generate_head(title='О чём всё это')
    body = generation_body(header='О чём всё это?')
    times = generate_numeration('Времена дня:', horoscope.times)
    advices = generate_numeration('Глаголы:', horoscope.advices)
    promises = generate_numeration('Обещания:', horoscope.promises)
    link = generate_link(text_link='Гороскоп')
    about_page = head + body + times + advices + promises + link

    about_open = open("about.html", "w")
    print(about_page, file=about_open)
    about_open.close()

save_about()
