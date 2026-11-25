// Public Supabase settings for the waitlist form.
// The anon key is designed to be public: Row Level Security on the
// "waitlist" table allows INSERT only (no SELECT, UPDATE or DELETE).
// Replace both values with the team project's values from
// Supabase Dashboard > Project Settings > API.
window.HELPENDZ_CONFIG = {
  supabaseUrl: "https://YOUR-PROJECT-REF.supabase.co",
  supabaseAnonKey: "YOUR-ANON-KEY"
};
