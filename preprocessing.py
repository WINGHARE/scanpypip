import scanpy.api as sc
import numpy as np
def receipe_my(adata,l_n_genes = 500, r_n_genes= 5000, log = False,sparse = False):

    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)

    if sparse == False:    
        adata.obs['n_counts'] = adata.X.sum(axis=1)
    else:
        adata.obs['n_counts'] = adata.X.sum(axis=1).A1

    adata = adata[
        np.logical_and(
        (adata.obs['n_genes'] > l_n_genes), 
        (adata.obs['n_genes'] < r_n_genes)),:]

    print(adata.shape)
    
    sc.pp.normalize_per_cell(adata, counts_per_cell_after=1e4)
    adata.raw = adata

    if log == True:
        sc.pp.log1p(adata)

    sc.pp.scale(adata, max_value=10)

    return adata
