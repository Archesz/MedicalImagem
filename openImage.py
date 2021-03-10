import nibabel as nib
import matplotlib.pyplot as plt

# Carregando os dados
epi_img = nib.load('someones_anatomy.nii')
epi_img_data = epi_img.get_fdata()
epi_img_data.shape

# Olhando as primeiras fatias na primeira, segunda e terceira dimensão.
def show_slices(slices):
  # Função para mostrar linhas das fatias de imagens
  fig, axes = plt.subplots(1, len(slices))
  for i, slice in enumerate(slices):
    axes[i].imshow(slice.T, cmap='gray', origin='lower')

slice_0 = epi_img_data[26, :, :]
slice_1 = epi_img_data[:, 30, :]
slice_2 = epi_img_data[:, :, 16]
show_slices([slice_0, slice_1, slice_2])
plt.suptitle('Imagens de Fatias Centrais')

n_i, n_j, n_k = epi_img_data.shape
center_i = (n_i - 1) // 2 
center_j = (n_j - 1) // 2
center_k = (n_k - 1) // 2
center_i, center_j, center_k
center_vox_value = epi_img_data[center_i, center_j, center_k]
center_vox_value
