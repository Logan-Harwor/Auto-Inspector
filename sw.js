const CACHE_NAME = 'auto-inspector-v1';
const ASSETS = [
    '/',               // This matches your index route
    '/manifest.json',
    '/icon-192.png',
    '/icon-512.png'
];

// Install Event
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(ASSETS))
    );
});

// Fetch Event - This is where the 404 usually happens
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Return the cached version, or try to get it from the network
                return response || fetch(event.request);
            })
    );
});