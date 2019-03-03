def remove_hashtags_and_links(list):
    return_list = []
    for i in list:
        return_list.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",i).split()))
    return return_list
