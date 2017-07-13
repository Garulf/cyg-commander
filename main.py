from wox import Wox,WoxAPI
# -*- coding: utf-8 -*-
import os.path,subprocess

class cygwin(Wox):

    def openUrl(self,cmd):
        swan = os.path.join('C:\\', 'cygwin64', 'bin', 'mintty.exe')
        subprocess.call([swan,'-h','never','-w','hide','-e','/bin/run.exe',swan,'--quote','-e','/bin/bash.exe','-l','-c','bash --init-file <(echo ". \"$HOME/.bashrc\";{0};history -r;history -s \'{0}\';history -a;history -w; pwd")'.format(cmd)],cwd='c:\\cygwin64')

    def query(self, query):
        results = []
        lines = ""
        user = os.getenv('username')
        with open('C:\\Users\\{0}\\AppData\\Roaming\\Swan\\.bash_history'.format(str(user))) as f:
            lines = f.readlines()
        argument = ""
        argument = query.lower().split()
        ico = './icons/console.png'
        #---handle connection errors
        if query == "":
            query_text = 'start typing to run your command HERE!'
        else:
            query_text = query
        results.append({
            "Title": 'RUN: {0}'.format(query_text),
            "SubTitle": 'Run this command in a new terminal.',
            "IcoPath":ico,
            "JsonRPCAction": {
                #change query to show only service type
                "method": "openUrl",
                "parameters": [query],
                # hide the query wox or not
                "dontHideAfterAction": False
            }
        })
        try:
            num_history = len(lines) - 10
            for l in range(len(lines) -1, int(num_history), -1):
                title = lines[l].rstrip('\n')
                if query.lower() in title.lower():
                    results.insert(l,{
                        "Title": title,
                        "SubTitle": 'Run this command in a new terminal.',
                        "IcoPath":ico,
                        "JsonRPCAction": {
                            #change query to show only service type
                            "method": "openUrl",
                            "parameters": [str(title)],
                            # hide the query wox or not
                            "dontHideAfterAction": False
                    }
                })
        except:
            pass
        return results

if __name__ == "__main__":
    cygwin()
