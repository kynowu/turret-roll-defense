# Rebuild www/index.html (offline, fonts embedded) from the web version
import base64,re
s=open('/home/claude/game/index.html').read()
fd='/home/claude/app/node_modules/@fontsource/'
def ff(fam,path,w):
    b=base64.b64encode(open(fd+path,'rb').read()).decode()
    return "@font-face{font-family:'%s';font-style:normal;font-weight:%s;font-display:block;src:url(data:font/woff2;base64,%s) format('woff2')}"%(fam,w,b)
css=ff('Black Ops One','black-ops-one/files/black-ops-one-latin-400-normal.woff2',400)+''.join(ff('Barlow Condensed','barlow-condensed/files/barlow-condensed-latin-%d-normal.woff2'%w,w) for w in (500,600,700))
s=re.sub(r'<link rel="preconnect"[^\n]*\n','',s)
s=re.sub(r'<link href="https://fonts.googleapis.com[^>]*>','<style>'+css+'</style>',s)
s=s.replace('user-scalable=no">','user-scalable=no,viewport-fit=cover">').replace('#hud{padding:8px 10px 6px;','#hud{padding:max(8px,env(safe-area-inset-top)) 10px 6px;')
assert 'googleapis' not in s
open('/home/claude/app/www/index.html','w').write(s)
print('synced',len(s)//1024,'KB')
