# Data Sources And Verification / 资料源与核验方式

Rental information changes fast. Use the skill's memory as a preference model and historical signal, not as live truth.

## Source Priority

1. Current official listing: price, availability, floorplan, amenities, parking policy, fees.
2. Recent resident reviews: Google Maps, Yelp, ApartmentRatings, Reddit, local forums.
3. Map and satellite view: roads, rail, stadiums, airports, public garages, delivery access.
4. Floorplan and site plan: floor, orientation, amenity exposure, hallway/elevator/trash/garage relationship.
5. Historical notes in this repo: useful for known patterns and user preferences, but must be rechecked.

## What Official Pages Are Good For

- Unit size, price, availability, listed amenities.
- In-unit laundry, A/C, dishwasher, parking type, package system names.
- Floorplan images and site maps.

## What Official Pages Are Weak For

- Car break-ins and garage tailgating.
- Package theft or damaged mailboxes.
- Thin walls, upstairs footsteps, false fire alarms.
- Management responsiveness during move-in, maintenance, disputes, and move-out.
- Actual food-delivery flow.

## Review Pattern Rules

- One severe review is a signal, not a verdict.
- Several recent reviews about the same issue are a pattern.
- A management response does not erase the issue unless residents later report resolution.
- A high rating with repeated severe low-star reviews should be treated as mixed.

## Geography Rules

- Do not rely on neighborhood names. Check actual map position.
- `0.4 mi` from rail can still matter if horns carry into the unit exposure.
- A building "near San Antonio" can mean shielded behind retail or exposed to San Antonio Rd; exact orientation matters.
- A high-rise can solve upstairs footsteps but still fail if low-floor street/public-garage exposure is bad.

## Privacy Rules

- Do not store raw leases, personal emails, phone numbers, names, or full screenshots with metadata.
- Summarize review patterns instead of copying long review text.
- Keep user-specific constraints as preferences, not identity details.
