import os, sys, httpx
from dotenv import load_dotenv
load_dotenv()

def translate(md, target='Indonesian'):
    prompt=f'Translate this technical Markdown to {target}. Preserve code blocks and headings.\n\n{md}'
    r=httpx.post(os.getenv('MIMO_URL','https://platform.xiaomimimo.com/v1/chat/completions'),headers={'Authorization':f"Bearer {os.getenv('MIMO_API_KEY','')}"},json={'model':os.getenv('MIMO_MODEL','mimo-v2.5'),'messages':[{'role':'user','content':prompt}]},timeout=120)
    data=r.json(); return data.get('choices',[{}])[0].get('message',{}).get('content',str(data))

if __name__=='__main__':
    path=sys.argv[1]; target=sys.argv[2] if len(sys.argv)>2 else 'Indonesian'
    print(translate(open(path,encoding='utf-8').read(), target))
