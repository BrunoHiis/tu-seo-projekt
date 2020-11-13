def write_output(website_url, date, outputLines):
    with open("output/" + website_url.replace("https://", "").replace("http://", "") + "_scan_" +  date + ".txt", "w") as the_file:
        for line in outputLines:
            the_file.write(line)
