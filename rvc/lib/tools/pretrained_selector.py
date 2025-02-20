import os


applio_dir = os.path.realpath(__file__)
applio_dir_len = applio_dir.find("Applio") + len("Applio")
applio_dir = applio_dir[:applio_dir_len]


def pretrained_selector(vocoder, sample_rate):
    base_path = os.path.join(applio_dir, "rvc", "models", "pretraineds", f"pretrained_{version}")

    path_g = os.path.join(base_path, f"f0G{str(sample_rate)[:2]}k.pth")
    path_d = os.path.join(base_path, f"f0D{str(sample_rate)[:2]}k.pth")

    if os.path.exists(path_g) and os.path.exists(path_d):
        return path_g, path_d
    else:
        return "", ""
