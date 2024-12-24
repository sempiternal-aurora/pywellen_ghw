from pywellen import Var, Hierarchy


def test(hier: Hierarchy, var: Var):
    print("Hello!", var.full_name(hier))
