resource "google_kms_key_ring" "secrets_key_ring" {
  project  = "${data.google_project.project.project_id}"
  name     = "secrets-key-ring"
  location = "global"
}

resource "google_kms_crypto_key" "firebase_key" {
  name     = "firebase-key"
  key_ring = "${google_kms_key_ring.secrets_key_ring.id}"
}