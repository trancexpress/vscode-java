import json
import sys

# compile stats e.g.:
# "name": "./node_modules/.pnpm/node-fetch@2.7.0/node_modules/node-fetch/lib/index.mjs",

# licence list e.g.:
#   "0BSD": [
#    {
#      "name": "tslib",
#      "versions": [
#        "1.14.1",
#        "2.8.1"
#      ],
#      "paths": [
#        "/home/sandreev/git/redhat/vscode-java/node_modules/.pnpm/tslib@1.14.1/node_modules/tslib",
#        "/home/sandreev/git/redhat/vscode-java/node_modules/.pnpm/tslib@2.8.1/node_modules/tslib"
#      ],
#      "license": "0BSD",
#      "author": "Microsoft Corp.",
#      "homepage": "https://www.typescriptlang.org/",
#      "description": "Runtime library for TypeScript helper functions"
#    }
#  ]

def collect_names(obj, results):
    if isinstance(obj, dict):
        if obj.get("codeGenerated") is True and "name" in obj:
            results.append(obj["name"])
        else:
            for value in obj.values():
                collect_names(value, results)
    elif isinstance(obj, list):
        for item in obj:
            collect_names(item, results)

def collect_repos(obj, modules, results):
    if isinstance(obj, dict):
        if "name" in obj and "paths" in obj and "homepage" in obj and "license" in obj and "versions" in obj:
            module = obj["name"]
            if module in modules:
                versions = obj["versions"]
                paths = obj["paths"]
                license = obj["license"]
                homepage = obj["homepage"]
                n = len(versions)
                for i in range(n):
                    results.append(module + "," + versions[i] + "," + license + "," + homepage + "," + paths[i])
        else:
            for key, value in obj.items():
                collect_repos(value, modules, results)
    elif isinstance(obj, list):
        for item in obj:
            collect_repos(item, modules, results)

def main():
    repos_path = sys.argv[1]
    stats_paths = sys.argv[2:]

    results = []
    for stats_path in stats_paths:
        with open(stats_path) as f:
            data = json.load(f)
            collect_names(data, results)

    modules = set()
    for name in results:
        if not name.startswith("./node_modules/"):
            continue
        s = name.split("/")
        module = s[5] # e.g.: ./node_modules/.pnpm/@vscode+codicons@0.0.32/node_modules/@vscode/codicons/
        if module.startswith("@"):
            module += "/" + s[6]
        modules.add(module)

    with open(repos_path) as f:
        data = json.load(f)
    results = []
    collect_repos(data, modules, results)

    sorted_modules = sorted(results)
    for module in sorted_modules:
        print(module)

main()
