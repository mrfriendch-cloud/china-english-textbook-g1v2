import os
import json
import asyncio
import edge_tts

VOICE = "en-US-AnaNeural"  # Friendly standard American voice for primary school English

async def generate_audio_for_item(text, output_file):
    if os.path.exists(output_file):
        print(f"Skipping existing: {output_file}")
        return
    print(f"Generating TTS for [{text}] -> {output_file}")
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)

async def main():
    audio_dir = "audio"
    os.makedirs(audio_dir, exist_ok=True)

    with open("pdf_structure.json", "r", encoding="utf-8") as f:
        pdf_data = json.load(f)

    manifest_entries = {}
    tasks = []

    for unit in pdf_data.get("units", []):
        unit_id = unit.get("id", "u0")
        
        # Process Vocabulary
        for item in unit.get("vocabulary", []):
            audio_id = item.get("audio")
            text = item.get("word")
            if audio_id and text:
                out_path = os.path.join(audio_dir, f"{audio_id}.mp3")
                manifest_entries[audio_id] = {
                    "text": text,
                    "translation": item.get("translation", ""),
                    "file": f"audio/{audio_id}.mp3",
                    "type": "vocabulary"
                }
                tasks.append(generate_audio_for_item(text, out_path))

        # Process Dialogues / Sentences
        for item in unit.get("dialogues", []):
            audio_id = item.get("audio")
            text = item.get("text")
            if audio_id and text:
                out_path = os.path.join(audio_dir, f"{audio_id}.mp3")
                manifest_entries[audio_id] = {
                    "text": text,
                    "translation": item.get("translation", ""),
                    "file": f"audio/{audio_id}.mp3",
                    "type": "dialogue"
                }
                tasks.append(generate_audio_for_item(text, out_path))

    if tasks:
        await asyncio.gather(*tasks)

    manifest_path = os.path.join(audio_dir, "audio_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({
            "voice": VOICE,
            "count": len(manifest_entries),
            "entries": manifest_entries
        }, f, ensure_ascii=False, indent=2)

    print(f"\nAudio generation completed! Generated manifest with {len(manifest_entries)} entries at {manifest_path}")

if __name__ == "__main__":
    asyncio.run(main())
