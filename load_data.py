
import os
import glob
from mne_bids import BIDSPath, read_raw_bids

def cargar_datos(bids_root, group_label):
    datos = []
    sujetos = glob.glob(os.path.join(bids_root, f"sub-{group_label}*"))

    for subj_path in sujetos:
        subj = os.path.basename(subj_path)
        sesiones = glob.glob(os.path.join(subj_path, "ses-*"))

        for ses_path in sesiones:
            ses = os.path.basename(ses_path)

            bids_path = BIDSPath(
                root=bids_root,
                subject=subj.replace("sub-", ""),
                session=ses.replace("ses-", ""),
                datatype="eeg", task="rest", suffix="eeg"
            )

            try:
                raw = read_raw_bids(bids_path, verbose=False)
                raw = raw.pick_channels(raw.ch_names[:32])
                datos.append(raw)
                print(f"✔️ Cargado: {subj} - {ses}")
            except FileNotFoundError:
                print(f"⚠️ No se encontró EEG para: {subj} - {ses}")

    return datos
