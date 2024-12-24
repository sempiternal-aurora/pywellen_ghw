from pywellen import Waveform


def explore_scope(hier, all_vars, scope):
    for var in scope.vars(hier):
        if var.full_name(hier) not in all_vars:
            print(f"Hierarchy.all_vars() missed variable {var.full_name(hier)}")
    for s in scope.scopes(hier):
        explore_scope(hier, all_vars, s)


def main(wellen: Waveform):
    all_vars = [var.full_name(wellen.hierarchy) for var in wellen.hierarchy.all_vars()]
    for scope in wellen.hierarchy.top_scopes():
        explore_scope(wellen.hierarchy, all_vars, scope)


if __name__ == "__main__":
    print("Testing GHW file")
    wellen = Waveform("CustomWrapper_tb.ghw")
    main(wellen)
    print("Testing vcd file")
    wellen = Waveform("CustomWrapper_tb.vcd")
    main(wellen)
