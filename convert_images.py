import os
from PIL import Image

def convert_images_to_webp(directory):
    print(f"Iniciando a conversão de imagens na pasta: {directory}")
    for root, dirs, files in os.walk(directory):
        for file in files:
            lower_file = file.lower()
            if lower_file.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(root, file)
                name, _ = os.path.splitext(file)
                webp_path = os.path.join(root, f"{name}.webp")
                
                print(f"Processando: {file}...")
                try:
                    with Image.open(img_path) as img:
                        # Para imagens RGBA (com transparência PNG), converte mantendo transparência ou RGB normal
                        if img.mode == 'RGBA':
                            # WebP suporta transparência nativa
                            img.save(webp_path, 'WEBP', quality=85)
                        else:
                            # Converte RGB
                            img.save(webp_path, 'WEBP', quality=80)
                    
                    size_orig = os.path.getsize(img_path) / 1024
                    size_webp = os.path.getsize(webp_path) / 1024
                    reduction = (1 - (size_webp / size_orig)) * 100
                    print(f"  -> Salvo como {name}.webp")
                    print(f"  -> Tamanho original: {size_orig:.2f} KB | Novo tamanho: {size_webp:.2f} KB | Redução: {reduction:.2f}%")
                except Exception as e:
                    print(f"  [ERRO] Falha ao converter {file}: {e}")

if __name__ == "__main__":
    # Caminho absoluto da pasta assets/images
    assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "images")
    if os.path.exists(assets_dir):
        convert_images_to_webp(assets_dir)
    else:
        print(f"Erro: diretório {assets_dir} não encontrado.")
