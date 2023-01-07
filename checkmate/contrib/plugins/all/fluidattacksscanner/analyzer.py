# -*- coding: utf-8 -*-


from checkmate.lib.analysis.base import BaseAnalyzer

import logging
import os
import tempfile
import json
import subprocess

logger = logging.getLogger(__name__)


class FluidAttacksAnalyzer(BaseAnalyzer):

    def __init__(self, *args, **kwargs):
        super(FluidAttacksAnalyzer, self).__init__(*args, **kwargs)

    def summarize(self, items):
        pass

    def analyze(self, file_revision):
        issues = []
        result = ""
        f = tempfile.NamedTemporaryFile(delete=False)
        fconf = tempfile.NamedTemporaryFile(delete=False)
        fresults = tempfile.NamedTemporaryFile(delete=False)

        try:
            with f:
                try:
                  f.write(file_revision.get_file_content())
                except UnicodeDecodeError:
                  pass
            f1 = open(fconf.name, "w")
            f1.write("namespace: repository\noutput:\n  file_path: ")
            f1.write(fresults.name+"\n")
            f1.write("  format: CSV\npath:\n  include:\n    - "+f.name)
            f1.close()
            os.chdir("/tmp")
            os.environ["PATH"] = "/root/.nix-profile/bin:/nix/var/nix/profiles/default/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            try:
                result = subprocess.check_output(["/root/.nix-profile/bin/m",
                                                  "gitlab:fluidattacks/universe@trunk",
                                                  "/skims",
                                                  "scan",
                                                  fconf.name],
                                                  stderr=subprocess.DEVNULL).strip()
            except subprocess.CalledProcessError as e:
                pass
            try:
                json_result = json.loads(result)
            except ValueError:
                json_result = {}
                pass

            my_file = open(fresults.name, 'r')
            data = my_file.readlines()
            firstLine = data.pop(0) 
            outjson = []
            val ={}
            for line in data:
              out=line.split(",")
              val["line"]=out[3]
              val["data"]=out[6]
              outjson.append(val)
              val={}

            try:
                for issue in outjson:
                  line = issue["line"]
                  line = int(line)
                  location = (((line, line),
                             (line, None)),)

                  if ".go" in file_revision.path or ".cs" in file_revision.path or ".java" in file_revision.path or ".js" in file_revision.path or ".ts" in file_revision.path:
                    issues.append({
                      'code': "I001",
                      'location': location,
                      'data': issue["data"],
                      'file': file_revision.path,
                      'line': line,
                      'fingerprint': self.get_fingerprint_from_code(file_revision, location, extra_data=issue["data"])
                    })

            except KeyError:
                pass

        finally:
            os.unlink(f.name)
        return {'issues': issues}
