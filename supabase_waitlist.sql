-- Run once in Supabase Dashboard > SQL Editor.
-- Creates an insert-only waitlist table for the landing page.
create table if not exists public.waitlist (
  id         bigint generated always as identity primary key,
  name       text not null check (char_length(name) between 1 and 80),
  contact    text not null check (char_length(contact) between 5 and 120),
  role       text not null check (role in ('customer','provider')),
  area       text not null check (area in ('Kalmunai','Nintavur','Other')),
  language   text not null default 'en' check (language in ('en','si','ta')),
  consent    boolean not null check (consent = true),
  created_at timestamptz not null default now()
);

alter table public.waitlist enable row level security;

-- The public (anon) key may only INSERT. No policy for SELECT, UPDATE
-- or DELETE exists, so the website can never read the list back.
create policy "anyone can join the waitlist"
  on public.waitlist for insert
  to anon
  with check (consent = true);
