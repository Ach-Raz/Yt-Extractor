import os
import sys
import urllib.request  # <<< CORREZIONE QUI: Importiamo il modulo intero


def download_youtube_thumbnail(url: str):
    """
    Estrae l'ID del video da un URL di YouTube e scarica il thumbnail
    direttamente dall'API di immagini di YouTube usando urllib.request.
    """
    print("----------------------------------------------")
    print("🛠️  Inizio download thumbnail (Metodo diretto)...")

    # 1. Estrarre l'ID del video
    video_id = None
    if "v=" in url:
        # Esempio: youtube.com/watch?v=ID&t=10s
        video_id = url.split("v=")[-1].split("&")[0]
    elif "embed/" in url:
        # Esempio: youtube.com/embed/ID
        video_id = url.split("embed/")[-1].split("?")[0]
    else:
        print("\n❌ ERRORE: URL non valido o non riconducibile a un ID video.")
        return

    # 2. Costruire l'URL del thumbnail di massima qualità (maxresdefault)
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

    # 3. Definire il percorso locale di salvataggio
    filename = f"{video_id}_thumbnail.jpg"
    output_path = os.path.join(os.getcwd(), filename)

    try:
        # Scarica l'immagine usando il modulo urllib.request
        urllib.request.urlretrieve(thumbnail_url, output_path)

        print("\n✅ Download completato con successo!")
        print("File salvato come:", output_path)

    except Exception as e:
        print(f"\n❌ ERRORE durante il download: {e}")
        print(
            "Suggerimento: Controlla la connettività o se YouTube ha cambiato il formato di immagini."
        )


if __name__ == "__main__":
    # 1. Ricevi l'URL dal parametro della riga di comando
    if len(sys.argv) > 1:
        youtube_url = sys.argv[1]
    else:
        # 2. Richiedi l'URL se non fornito
        youtube_url = input("Inserisci l'URL di YouTube: ").strip()

    if youtube_url:
        download_youtube_thumbnail(youtube_url)
    else:
        print("Nessun URL fornito. Script terminato.")
