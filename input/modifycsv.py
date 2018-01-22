file=open('old.articles.csv.old','r')
out=open('new.csv','w')
for line in file:
    lines=line
    url_index=line.find('http')-1
    lines=lines[0:10]+lines[10:url_index].replace(',','，')+lines[url_index:]
    out.write(lines)
