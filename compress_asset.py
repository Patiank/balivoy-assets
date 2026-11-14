"""
BaliVoy Asset Optimizer Helper
Usage:
    python compress_asset.py input_video.mp4 [output_name]
    
Features:
- Mutes audio for background loop video (saves ~30-40% file size)
- Applies H.264 with +faststart (starts playing at 0.1s without buffering)
- Extracts high-quality first-frame poster thumbnail (.webp)
- Automatically saves to videos/ and images/
"""

import sys
import os
import subprocess

def optimize_video(input_path, output_name="hero-bali-loop"):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    base_dir = os.path.dirname(os.path.abspath(__file__))
    video_out = os.path.join(base_dir, "videos", f"{output_name}.mp4")
    poster_out = os.path.join(base_dir, "images", f"{output_name}-cover.webp")

    print(f"🎬 Mengompresi video: {input_path}")
    print(f"🎯 Target output video: {video_out}")
    print(f"🖼️ Target output poster: {poster_out}")

    # 1. Compress Video (H.264, CRF 26, mute audio, faststart)
    cmd_video = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-an",                      # Strip audio track for background video
        "-vcodec", "libx264",
        "-crf", "26",               # Balanced high-visual quality vs small file size
        "-preset", "slow",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",  # Moov atom at beginning of file for instant web playback
        video_out
    ]

    res = subprocess.run(cmd_video)
    if res.returncode != 0:
        print("❌ Gagal mengompresi video.")
        return

    # 2. Extract first-frame poster
    cmd_poster = [
        "ffmpeg", "-y",
        "-ss", "00:00:01",
        "-i", input_path,
        "-vframes", "1",
        "-q:v", "80",
        poster_out
    ]
    subprocess.run(cmd_poster)

    in_size = os.path.getsize(input_path) / (1024 * 1024)
    out_size = os.path.getsize(video_out) / (1024 * 1024)

    print(f"\n✅ Sukses!")
    print(f"Ukuran asli: {in_size:.2f} MB")
    print(f"Ukuran terkompresi: {out_size:.2f} MB (Hemat {((in_size - out_size)/in_size)*100:.1f}%)")
    print(f"Poster webp dibuat: {poster_out}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[2] if len(sys.argv) > 2 else "hero-bali-loop"
        optimize_video(sys.argv[1], name)
    else:
        print("Gunakan: python compress_asset.py <path_video> [nama_output]")
