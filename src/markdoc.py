import pdoc
import lib
from pathlib import Path
from pkgutil import iter_modules

def pdf(modules):
    pdf = pdoc._render_template('pdf.mako', modules=modules)
    return pdf

def list_submodules(module):
    submodule_name = []
    for submodule in iter_modules(module.__path__):
        submodule_name.append(submodule.name)
    return submodule_name


if __name__ == "__main__":
    
    modules = [ 'lib.' + i for i in list_submodules(lib) ]  # Public submodules are auto-imported

    context = pdoc.Context()
    # print(pdoc.tpl_lookup.directories)
    modules = [pdoc.Module(mod, context=context)
           for mod in modules]
    pdoc.link_inheritance(context)

    pd = pdf(modules)
    md_path = Path('doc/lib.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(pd)
