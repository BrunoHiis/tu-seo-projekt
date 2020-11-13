from bs4 import BeautifulSoup


def meta_tags(html):
    meta_description_response = "Does not have meta description!"
    meta_keywords_response = "Does not have any meta keywords!"

    try:
        for link in html.find_all('meta'):
            # check if has meta description
            if(link.get('name') == 'description'):
                if len(link.get('content')) < 160 and len(link.get('content')) > 50:
                    meta_description_response = "Good size meta description."
                elif len(link.get('content')) < 160:
                    meta_description_response = "Too big meta description."
                else:
                    meta_description_response = "Too small meta description!"
            # check if has meta keywords
            if(link.get('name') == 'keywords'):
                keyword_array_length = len(link.get('content').split(","))
                if keyword_array_length < 10 and keyword_array_length > 5:
                    meta_keywords_response = "Good amount of meta keywords."
                elif keyword_array_length > 10:
                    meta_keywords_response = "Too many meta keywords."
                else:
                    meta_keywords_response = "Not enough meta keywords."

    except:
        print("Could not get page data.")

    return {"description": meta_description_response, "keywords": meta_keywords_response}


def multiple_h1(html):
    h1_response = "Does not have any h1 elements!"

    try:
        if len(html.select('h1')) > 1:
            h1_response = "Has too many H1 elements. Try to not have over 1 H1 element per page."
        elif len(html.select('h1')) == 1:
            h1_response = "Has one H1 element."
    except:
        print("Could not get page data.")

    return h1_response


def alt_texts(html):
    alt_texts_response = "Page does not have any images."

    try:
        imagesCount = 0
        imagesWithAltCount = 0

        for img in html.find_all('img'):
            imagesCount += 1

            # check if image has alt text
            if img.get('alt'):
                # get alt text length
                if len(img["alt"]) > 3:
                    imagesWithAltCount += 1

        if(not imagesCount == 0):
            if((imagesCount - imagesWithAltCount) == 0):
                alt_texts_response = "All images have alt texts."
            elif(imagesWithAltCount == 0):
                alt_texts_response = "All images are missing alt texts!"
            else:
                alt_texts_response = "Some images are missing alt texts!"

    except:
        print("Could not get page data.")

    return alt_texts_response


def check_titles(html):
    title_response = "Page does not have a title."

    try:
        title_len = len(html.select_one('title').text)

        if title_len > 49 and title_len < 61:
            title_response = "Perfect title length."
        elif title_len < 49:
            title_response = "Title too short."
        elif title_len > 61:
            title_response = "Title too big."
    except:
        print("Could not get page data.")

    return title_response
