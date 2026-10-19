# Profile reference review — 19 October 2026

Source: [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme). The supplied attachment was a text-only copy; source links were recovered from the live directory.

Scope: **240 distinct repository references** (242 category/tool entries before deduplication). **237 READMEs retrieved**, including renamed repositories, lowercase filenames and an organization profile. Two references return 404 (`maddhruv/maddhruv`, `Wrapperup/Wrapperup`); `teoxoy/teoxoy` is currently an empty archived repository. These three could not be assessed. Articles and videos are not additional repositories and are outside this repository ledger.

This is a presentation and documented-mechanism review, not a line-by-line implementation audit of 240 codebases. Signals below come from README markup and setup instructions. Executable source was additionally inspected for Simon Willison’s build workflow and snake-and-commits’ composite action; third-party code was not copied or executed. GitHub metadata and the five selected project READMEs were read to ground the implemented portfolio content.

## What the patterns mean

- Profile READMEs render Markdown, permitted HTML and images. Expandable `details` sections work natively. Arbitrary JavaScript does not run inside the README.
- Interactive chess/tic-tac-toe profiles use links that open issues, then automation validates a move and regenerates the board. They are not JavaScript games embedded in Markdown.
- Typing, gravity, snake, bonsai and cat visuals are usually rendered to SVG/GIF and served as images. API-backed cards depend on availability, caching, credentials and rate limits.
- Self-updating profiles fetch source data on a schedule, replace marked README regions and commit generated output. This is the mechanism adopted for Kazi’s public project snapshot.
- A portfolio website can offer direct client-side interactions; the new explorer uses a fixed command vocabulary and native inputs, with full project content in the HTML.

## Adoption decisions

| Reference | Useful idea | Implemented adaptation |
| --- | --- | --- |
| [simonw/simonw](https://github.com/simonw/simonw) | Generated, source-linked evidence in a bounded README region | Weekly workflow and Python standard-library generator for five public project snapshots; preserves previous evidence on fetch failure |
| [DenverCoder1/DenverCoder1](https://github.com/DenverCoder1/DenverCoder1) | Project grouping, collapsible depth and a recognizable visual identity | Source-linked cards, expandable implementation/limits and an original repository-hosted SVG banner |
| [MacroPower/MacroPower](https://github.com/MacroPower/MacroPower) | Scannable role and technology organization | Discipline and technology filters tied to inspectable projects |
| [BrunnerLivio/BrunnerLivio](https://github.com/BrunnerLivio/BrunnerLivio), [fnky/fnky](https://github.com/fnky/fnky) | Memorable terminal/retro presentation | An accessible terminal-style portfolio navigation panel; fixed commands and ordinary browse controls |
| [dahan8473/snake-and-commits](https://github.com/dahan8473/snake-and-commits) | Locally generated animated SVG and reduced-motion fallback | Original animated delivery-loop SVG; no third-party action or contribution claim copied |
| [rafaeloliveiraz/gitglance](https://github.com/rafaeloliveiraz/gitglance), [icortesb/vinilo](https://github.com/icortesb/vinilo) | Own generated assets to reduce shared-endpoint dependence | Profile assets and JSON snapshot committed in the owner’s repository |
| [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats) | Popular dynamic statistics pattern | Reviewed; its README now directs users to successor projects. No new dependency on that hosted card service |
| [timburgan/timburgan](https://github.com/timburgan/timburgan), [DoubleGremlin181/DoubleGremlin181](https://github.com/DoubleGremlin181/DoubleGremlin181) | Participation through visible choices | Adapted as direct project-navigation commands on the website; no new issue-triggered game workflow |

Visitor counters, coding-time providers, Spotify, Todoist, zodiac cards, artificial contribution art and guestbooks were reviewed but not installed. They either require account connections/data not established here or contribute less to the current hiring and consulting goals. Project ranks and streaks are not used as competence claims.

## Repository-by-repository ledger

The purpose column identifies whether an entry is a personal presentation or a reusable tool. The observation column records concrete README mechanisms; it is not a runtime compatibility guarantee. For personal profiles, the category is the directory’s classification. Linked names resolve to the current repository when a rename was verified.

| Repository | Main purpose / presentation | Observed mechanism / reuse decision |
| --- | --- | --- |
| [abhisheknaiidu/abhisheknaiidu](https://github.com/abhisheknaiidu/abhisheknaiidu) | Personal profile · GitHub Actions 🤖 | Generated content markers, External statistics cards |
| [thmsgbrt/thmsgbrt](https://github.com/thmsgbrt/thmsgbrt) | Personal profile · GitHub Actions 🤖 | SVG imagery, GIF imagery, Structured tables |
| [bdougie/bdougie](https://github.com/bdougie/bdougie) | Personal profile · GitHub Actions 🤖 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [sw-yx/sw-yx](https://github.com/swyxio/swyxio) | Personal profile · GitHub Actions 🤖 | SVG imagery, Generated content markers, Issue-based interaction; renamed from sw-yx/sw-yx |
| [simonw/simonw](https://github.com/simonw/simonw) | Personal profile · GitHub Actions 🤖 | SVG imagery, Generated content markers, Structured tables |
| [mscoutermarsh/mscoutermarsh](https://github.com/mscoutermarsh/mscoutermarsh) | Personal profile · GitHub Actions 🤖 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [mokkapps/mokkapps](https://github.com/mokkapps/mokkapps) | Personal profile · GitHub Actions 🤖 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [athul/athul](https://github.com/athul/athul) | Personal profile · GitHub Actions 🤖 | Generated content markers |
| [gautamkrishnar/gautamkrishnar](https://github.com/gautamkrishnar/gautamkrishnar) | Personal profile · GitHub Actions 🤖 | Expandable sections, SVG imagery, GIF imagery, Structured tables |
| [roaldnefs/roaldnefs](https://github.com/roaldnefs/roaldnefs) | Personal profile · GitHub Actions 🤖 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [mopig/mopig](https://github.com/mopig/mopig) | Personal profile · GitHub Actions 🤖 | Expandable sections, SVG imagery, External statistics cards |
| [maddhruv/maddhruv](https://github.com/maddhruv/maddhruv) | Unavailable reference | Not assessed; 404 |
| [guilyx/guilyx](https://github.com/guilyx/guilyx) | Personal profile · GitHub Actions 🤖 | GIF imagery |
| [JessicaLim8/JessicaLim8](https://github.com/JessicaLim8/JessicaLim8) | Personal profile · GitHub Actions 🤖 | Issue-based interaction |
| [tw93/tw93](https://github.com/tw93/tw93) | Personal profile · GitHub Actions 🤖 | GIF imagery, Generated content markers, Structured tables |
| [liununu/liununu](https://github.com/liununu/liununu) | Personal profile · GitHub Actions 🤖 | SVG imagery |
| [qu4k/qu4k](https://github.com/notfilippo/notfilippo) | Personal profile · GitHub Actions 🤖 | Plain prose, links or image-led identity; no automation mechanism established from README; renamed from qu4k/qu4k |
| [moepoi/moepoi](https://github.com/moepoi/moepoi) | Personal profile · GitHub Actions 🤖 | Expandable sections, SVG imagery, External statistics cards |
| [blackcater/blackcater](https://github.com/blackcater/blackcater) | Personal profile · GitHub Actions 🤖 | SVG imagery, GIF imagery |
| [Spiderpig86/Spiderpig86](https://github.com/Spiderpig86/Spiderpig86) | Personal profile · GitHub Actions 🤖 | Expandable sections, SVG imagery, GIF imagery, External statistics cards |
| [gargakshit/gargakshit](https://github.com/gargakshit/gargakshit) | Personal profile · GitHub Actions 🤖 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [ouuan/ouuan](https://github.com/ouuan/ouuan) | Personal profile · GitHub Actions 🤖 | Generated content markers, External statistics cards, Structured tables |
| [d-koppenhagen/d-koppenhagen](https://github.com/d-koppenhagen/d-koppenhagen) | Personal profile · GitHub Actions 🤖 | Structured tables |
| [vidyabhandary/vidyabhandary](https://github.com/vidyabhandary/vidyabhandary) | Personal profile · GitHub Actions 🤖 | SVG imagery, Generated content markers, Structured tables |
| [RaoHai/RaoHai](https://github.com/RaoHai/RaoHai) | Personal profile · GitHub Actions 🤖 | GIF imagery |
| [jatin2003/jatin2003](https://github.com/jatin2003/jatin2003) | Personal profile · GitHub Actions 🤖 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [teoxoy/teoxoy](https://github.com/teoxoy/teoxoy) | Empty archived profile repository | Root directory has no files; no README to inspect |
| [aralroca/aralroca](https://github.com/aralroca/aralroca) | Personal profile · GitHub Actions 🤖 | SVG imagery, External statistics cards, Structured tables |
| [codestackr/codestackr](https://github.com/codestackr/codestackr) | Personal profile · GitHub Actions 🤖 | Expandable sections, SVG imagery, Generated content markers, External statistics cards |
| [itgoyo/itgoyo](https://github.com/itgoyo/itgoyo) | Personal profile · GitHub Actions 🤖 | Expandable sections, SVG imagery, Generated content markers |
| [lifeparticle/lifeparticle](https://github.com/lifeparticle/lifeparticle) | Personal profile · GitHub Actions 🤖 | SVG imagery |
| [timburgan/timburgan](https://github.com/timburgan/timburgan) | Personal profile · Game Mode 🚀 | Issue-based interaction, Structured tables; game interaction documented; no game workflow adopted |
| [benjaminsampica/benjaminsampica](https://github.com/benjaminsampica/benjaminsampica) | Personal profile · Game Mode 🚀 | Issue-based interaction, Structured tables; game interaction documented; no game workflow adopted |
| [DoubleGremlin181/DoubleGremlin181](https://github.com/DoubleGremlin181/DoubleGremlin181) | Personal profile · Game Mode 🚀 | Structured tables; game interaction documented; no game workflow adopted |
| [JonathanGin52/JonathanGin52](https://github.com/JonathanGin52/JonathanGin52) | Personal profile · Game Mode 🚀 | Issue-based interaction, Structured tables; game interaction documented; no game workflow adopted |
| [rossjrw/rossjrw](https://github.com/rossjrw/rossjrw) | Personal profile · Game Mode 🚀 | Expandable sections, SVG imagery, Issue-based interaction, Structured tables; game interaction documented; no game workflow adopted |
| [kylepls/kylepls](https://github.com/kylepls/kylepls) | Personal profile · Game Mode 🚀 | Plain prose, links or image-led identity; no automation mechanism established from README; game interaction documented; no game workflow adopted |
| [HFO4/HFO4](https://github.com/HFO4/HFO4) | Personal profile · Game Mode 🚀 | Expandable sections, SVG imagery; game interaction documented; no game workflow adopted |
| [marcizhu/marcizhu](https://github.com/marcizhu/marcizhu) | Personal profile · Game Mode 🚀 | Expandable sections, SVG imagery, Issue-based interaction, Structured tables; game interaction documented; no game workflow adopted |
| [Thaiane/Thaiane](https://github.com/Thaiane/Thaiane) | Personal profile · Code Mode 👨🏽‍💻 | GIF imagery; code-form biography is a presentation choice |
| [ashbakernz/ashbakernz](https://github.com/justashton/justashton) | Personal profile · Code Mode 👨🏽‍💻 | Plain prose, links or image-led identity; no automation mechanism established from README; code-form biography is a presentation choice; renamed from ashbakernz/ashbakernz |
| [anmol098/anmol098](https://github.com/anmol098/anmol098) | Personal profile · Code Mode 👨🏽‍💻 | SVG imagery, GIF imagery, Generated content markers; code-form biography is a presentation choice |
| [monkindey/monkindey](https://github.com/monkindey/monkindey) | Personal profile · Code Mode 👨🏽‍💻 | Plain prose, links or image-led identity; no automation mechanism established from README; code-form biography is a presentation choice |
| [ddroid/ddroid](https://github.com/ddroid/ddroid) | Personal profile · Code Mode 👨🏽‍💻 | Expandable sections, GIF imagery, Structured tables; code-form biography is a presentation choice |
| [martonlederer/martonlederer](https://github.com/martonlederer/old-profile-readme) | Personal profile · Code Mode 👨🏽‍💻 | SVG imagery; code-form biography is a presentation choice; renamed from martonlederer/martonlederer |
| [rednafi/rednafi](https://github.com/rednafi/rednafi) | Personal profile · Code Mode 👨🏽‍💻 | Structured tables; code-form biography is a presentation choice |
| [Zhenye-Na/Zhenye-Na](https://github.com/Zhenye-Na/Zhenye-Na) | Personal profile · Code Mode 👨🏽‍💻 | SVG imagery, External statistics cards; code-form biography is a presentation choice |
| [anuraghazra/anuraghazra](https://github.com/anuraghazra/anuraghazra) | Personal profile · Dynamic Realtime 💫 | SVG imagery, External statistics cards, Structured tables |
| [DenverCoder1/DenverCoder1](https://github.com/DenverCoder1/DenverCoder1) | Personal profile · Dynamic Realtime 💫 | Expandable sections, SVG imagery, Generated content markers, External statistics cards, Structured tables |
| [8bithemant/8bithemant](https://github.com/mayhemantt/mayhemantt) | Personal profile · Dynamic Realtime 💫 | SVG imagery, GIF imagery, External statistics cards, Structured tables; renamed from 8bithemant/8bithemant |
| [kittinan/kittinan](https://github.com/kittinan/kittinan) | Personal profile · Dynamic Realtime 💫 | External statistics cards |
| [novatorem/novatorem](https://github.com/novatorem/novatorem) | Personal profile · Dynamic Realtime 💫 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [C9-LinkRs/C9-LinkRs](https://github.com/jvillegasd/Jvillegasd) | Personal profile · Simple but Innovative Ones 🤗 | Plain prose, links or image-led identity; no automation mechanism established from README; renamed from C9-LinkRs/C9-LinkRs |
| [andyruwruw/andyruwruw](https://github.com/andyruwruw/andyruwruw) | Personal profile · Dynamic Realtime 💫 | SVG imagery |
| [rusty-sj/rusty-sj](https://github.com/rusty-sj/rusty-sj) | Personal profile · Dynamic Realtime 💫 | External statistics cards |
| [MacroPower/MacroPower](https://github.com/MacroPower/MacroPower) | Personal profile · Dynamic Realtime 💫 | SVG imagery, Generated content markers, Structured tables |
| [zumrudu-anka/zumrudu-anka](https://github.com/zumrudu-anka/zumrudu-anka) | Personal profile · Dynamic Realtime 💫 | SVG imagery, External statistics cards |
| [iampavangandhi/iampavangandhi](https://github.com/iampavangandhi/iampavangandhi) | Personal profile · Dynamic Realtime 💫 | Expandable sections, SVG imagery, GIF imagery, External statistics cards |
| [daniakash/daniakash](https://github.com/daniakash/daniakash) | Personal profile · Dynamic Realtime 💫 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [rahul-jha98/rahul-jha98](https://github.com/rahul-jha98/rahul-jha98) | Personal profile · Dynamic Realtime 💫 | SVG imagery, GIF imagery |
| [HwangTaehyun/HwangTaehyun](https://github.com/HwangTaehyun/HwangTaehyun) | Personal profile · Dynamic Realtime 💫 | External statistics cards |
| [nisarg1212/nisarg1212](https://github.com/nisarg1212/nisarg1212) | Personal profile · Dynamic Realtime 💫 | SVG imagery, Structured tables |
| [Raymo111/Raymo111](https://github.com/Raymo111/Raymo111) | Personal profile · A Little Bit of Everything 😃 | SVG imagery, GIF imagery, Generated content markers, Structured tables |
| [MartinHeinz/MartinHeinz](https://github.com/MartinHeinz/MartinHeinz) | Personal profile · A Little Bit of Everything 😃 | GIF imagery, External statistics cards |
| [adamalston/adamalston](https://github.com/adamalston/adamalston) | Personal profile · A Little Bit of Everything 😃 | SVG imagery |
| [rafnixg/rafnixg](https://github.com/rafnixg/rafnixg) | Personal profile · A Little Bit of Everything 😃 | SVG imagery |
| [sciencepal/sciencepal](https://github.com/sciencepal/sciencepal) | Personal profile · A Little Bit of Everything 😃 | SVG imagery, GIF imagery, External statistics cards |
| [hedythedev/hedythedev](https://github.com/hedyhli/hedyhli) | Personal profile · A Little Bit of Everything 😃 | Plain prose, links or image-led identity; no automation mechanism established from README; renamed from hedythedev/hedythedev |
| [xunzhuo/xunzhuo](https://github.com/xunzhuo/xunzhuo) | Personal profile · A Little Bit of Everything 😃 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [khalby786/khalby786](https://github.com/khalby786/khalby786) | Personal profile · A Little Bit of Everything 😃 | Expandable sections, Generated content markers, External statistics cards |
| [apoorvtyagi/apoorvtyagi](https://github.com/apoorvtyagi/apoorvtyagi) | Personal profile · A Little Bit of Everything 😃 | SVG imagery, GIF imagery, Generated content markers, External statistics cards |
| [cxyfreedom/cxyfreedom](https://github.com/cxyfreedom/cxyfreedom) | Personal profile · A Little Bit of Everything 😃 | SVG imagery, Generated content markers, External statistics cards |
| [minoveaz/minoveaz](https://github.com/minoveaz/minoveaz) | Personal profile · A Little Bit of Everything 😃 | SVG imagery, Generated content markers, External statistics cards |
| [AbhishekMaira10/AbhishekMaira10](https://github.com/AbhishekMaira10/AbhishekMaira10) | Personal profile · A Little Bit of Everything 😃 | Expandable sections, SVG imagery, GIF imagery, External statistics cards |
| [claytonjhamilton/claytonjhamilton](https://github.com/claytonjhamilton/claytonjhamilton) | Personal profile · A Little Bit of Everything 😃 | SVG imagery, GIF imagery |
| [syrashid/syrashid](https://github.com/syrashid/syrashid) | Personal profile · A Little Bit of Everything 😃 | GIF imagery |
| [cheesits456/cheesits456](https://github.com/cheesits456/cheesits456) | Personal profile · A Little Bit of Everything 😃 | GIF imagery, Generated content markers, External statistics cards |
| [Jackyu-1999/Jackyu-1999](https://github.com/Jackyu-1999/Jackyu-1999) | Personal profile · A Little Bit of Everything 😃 | SVG imagery, Generated content markers, External statistics cards |
| [raklaptudirm/raklaptudirm](https://github.com/raklaptudirm/raklaptudirm) | Personal profile · A Little Bit of Everything 😃 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [trinib/trinib](https://github.com/trinib/trinib) | Personal profile · A Little Bit of Everything 😃 | Expandable sections, SVG imagery, GIF imagery, External statistics cards, Issue-based interaction, Structured tables |
| [holic-x/holic-x](https://github.com/holic-x/holic-x) | Personal profile · A Little Bit of Everything 😃 | SVG imagery, Generated content markers, External statistics cards |
| [Magrelaio/Magrelaio](https://github.com/Magrelaio/Magrelaio) | Personal profile · A Little Bit of Everything 😃 | GIF imagery, Structured tables |
| [filiptronicek/filiptronicek](https://github.com/filiptronicek/filiptronicek) | Personal profile · Descriptive 🗒 | Expandable sections, External statistics cards, Structured tables |
| [garimasingh128/garimasingh128](https://github.com/garimasingh128/garimasingh128) | Personal profile · Descriptive 🗒 | SVG imagery, GIF imagery |
| [lizheming/lizheming](https://github.com/lizheming/lizheming) | Personal profile · Descriptive 🗒 | GIF imagery, External statistics cards, Structured tables |
| [you-create/you-create](https://github.com/cszach/cszach) | Personal profile · Descriptive 🗒 | Plain prose, links or image-led identity; no automation mechanism established from README; renamed from you-create/you-create |
| [sakshamtaneja21/sakshamtaneja21](https://github.com/sakshamtaneja21/sakshamtaneja21) | Personal profile · Descriptive 🗒 | GIF imagery, External statistics cards |
| [theabbie/theabbie](https://github.com/theabbie/theabbie) | Personal profile · Descriptive 🗒 | SVG imagery, Structured tables |
| [keshavsingh4522/keshavsingh4522](https://github.com/keshavsingh3197/keshavsingh3197) | Personal profile · Descriptive 🗒 | Expandable sections, SVG imagery, GIF imagery, Generated content markers, External statistics cards, Structured tables; renamed from keshavsingh4522/keshavsingh4522 |
| [vidursatija/vidursatija](https://github.com/vidursatija/vidursatija) | Personal profile · Descriptive 🗒 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [dayyass/dayyass](https://github.com/dayyass/dayyass) | Personal profile · Descriptive 🗒 | External statistics cards, Structured tables |
| [Nanra/Nanra](https://github.com/Nanra/Nanra) | Personal profile · Descriptive 🗒 | SVG imagery, External statistics cards |
| [natemoo-re/natemoo-re](https://github.com/natemoo-re/natemoo-re) | Personal profile · Simple but Innovative Ones 🤗 | Structured tables |
| [jh3y/jh3y](https://github.com/jh3y/jh3y) | Personal profile · Simple but Innovative Ones 🤗 | SVG imagery |
| [WaylonWalker/WaylonWalker](https://github.com/WaylonWalker/WaylonWalker) | Personal profile · Simple but Innovative Ones 🤗 | Expandable sections, SVG imagery, Structured tables |
| [vanshkapoor/vanshkapoor](https://github.com/vanshkapoor/vanshkapoor) | Personal profile · Simple but Innovative Ones 🤗 | SVG imagery |
| [harshkumarkhatri/harshkumarkhatri](https://github.com/harshkumarkhatri/harshkumarkhatri) | Personal profile · Simple but Innovative Ones 🤗 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [stephenajulu/stephenajulu](https://github.com/stephenajulu/stephenajulu) | Personal profile · Simple but Innovative Ones 🤗 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [MarikIshtar007/MarikIshtar007](https://github.com/MarikIshtar007/MarikIshtar007) | Personal profile · Simple but Innovative Ones 🤗 | SVG imagery, GIF imagery, External statistics cards |
| [ashleymavericks/ashleymavericks](https://github.com/ashleymavericks/ashleymavericks) | Personal profile · Simple but Innovative Ones 🤗 | Expandable sections, SVG imagery, GIF imagery, Structured tables |
| [Rishit-dagli/Rishit-dagli](https://github.com/Rishit-dagli/Rishit-dagli) | Personal profile · Simple but Innovative Ones 🤗 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [vinitshahdeo/vinitshahdeo](https://github.com/vinitshahdeo/vinitshahdeo) | Personal profile · Simple but Innovative Ones 🤗 | SVG imagery, External statistics cards, Structured tables |
| [f/f](https://github.com/f/f) | Personal profile · Simple but Innovative Ones 🤗 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [lucasvazq/lucasvazq](https://github.com/lucasvazq/lucasvazq) | Personal profile · Simple but Innovative Ones 🤗 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [jaywcjlove/jaywcjlove](https://github.com/jaywcjlove/jaywcjlove) | Personal profile · Simple but Innovative Ones 🤗 | Expandable sections, SVG imagery, External statistics cards, Structured tables |
| [halfrost/halfrost](https://github.com/halfrost/halfrost) | Personal profile · Simple but Innovative Ones 🤗 | Expandable sections, GIF imagery, External statistics cards |
| [sriharikapu/sriharikapu](https://github.com/sriharikapu/sriharikapu) | Personal profile · Simple but Innovative Ones 🤗 | SVG imagery, External statistics cards, Issue-based interaction |
| [vaaski/vaaski](https://github.com/vaaski/vaaski) | Personal profile · Simple but Innovative Ones 🤗 | SVG imagery |
| [arturssmirnovs/arturssmirnovs](https://github.com/arturssmirnovs/arturssmirnovs) | Personal profile · Simple but Innovative Ones 🤗 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [Terabyte17/Terabyte17](https://github.com/Terabyte17/Terabyte17) | Personal profile · Simple but Innovative Ones 🤗 | SVG imagery, GIF imagery, External statistics cards |
| [Defcon27/Defcon27](https://github.com/Defcon27/Defcon27) | Personal profile · Simple but Innovative Ones 🤗 | Expandable sections, SVG imagery, GIF imagery, External statistics cards |
| [techytushar/techytushar](https://github.com/techytushar/techytushar) | Personal profile · Simple but Innovative Ones 🤗 | SVG imagery, GIF imagery, External statistics cards, Structured tables |
| [onimur/onimur](https://github.com/onimur/onimur) | Personal profile · Simple but Innovative Ones 🤗 | SVG imagery, External statistics cards |
| [brunotacca/brunotacca](https://github.com/brunotacca/brunotacca) | Personal profile · Simple but Innovative Ones 🤗 | Expandable sections, SVG imagery, External statistics cards, Structured tables |
| [Wrapperup/Wrapperup](https://github.com/Wrapperup/Wrapperup) | Unavailable reference | Not assessed; 404 |
| [alihamzaio/alihamzaio](https://github.com/alihamzaio/alihamzaio) | Personal profile · Simple but Innovative Ones 🤗 | Structured tables |
| [matyo91/matyo91](https://github.com/matyo91/matyo91) | Personal profile · Typing.. Mode 🎰 | GIF imagery, Issue-based interaction; animation is presentational, not executable README JavaScript |
| [CyrisXD/CyrisXD](https://github.com/CyrisXD/CyrisXD) | Personal profile · Typing.. Mode 🎰 | SVG imagery, GIF imagery, External statistics cards; animation is presentational, not executable README JavaScript |
| [mmphego/mmphego](https://github.com/mmphego/mmphego) | Personal profile · Typing.. Mode 🎰 | SVG imagery, GIF imagery, Structured tables; animation is presentational, not executable README JavaScript |
| [ABSphreak/ABSphreak](https://github.com/ABSphreak/ABSphreak) | Personal profile · Typing.. Mode 🎰 | SVG imagery, GIF imagery, External statistics cards; animation is presentational, not executable README JavaScript |
| [MasonSlover/MasonSlover](https://github.com/MasonSlover/MasonSlover) | Personal profile · Typing.. Mode 🎰 | GIF imagery; animation is presentational, not executable README JavaScript |
| [SuperSupeng/SuperSupeng](https://github.com/SuperSupeng/SuperSupeng) | Personal profile · Typing.. Mode 🎰 | SVG imagery, Structured tables; animation is presentational, not executable README JavaScript |
| [innng/innng](https://github.com/innng/innng) | Personal profile · Anime 👾 | GIF imagery |
| [edisonlee55/edisonlee55](https://github.com/yuna0x0/yuna0x0) | Personal profile · Anime 👾 | Plain prose, links or image-led identity; no automation mechanism established from README; renamed from edisonlee55/edisonlee55 |
| [Xx-Ashutosh-xX/Xx-Ashutosh-xX](https://github.com/Xx-Ashutosh-xX/Xx-Ashutosh-xX) | Personal profile · Anime 👾 | GIF imagery, External statistics cards |
| [PrincessAkira/PrincessAkira](https://github.com/HerXayah/HerXayah) | Personal profile · Anime 👾 | SVG imagery, GIF imagery; renamed from PrincessAkira/PrincessAkira |
| [caneco/caneco](https://github.com/caneco/caneco) | Personal profile · Minimalistic ✨ | SVG imagery; useful restraint for first-screen positioning |
| [lauragift21/lauragift21](https://github.com/lauragift21/lauragift21) | Personal profile · Minimalistic ✨ | GIF imagery; useful restraint for first-screen positioning |
| [PluckyPrecious/PluckyPrecious](https://github.com/PluckyPrecious/PluckyPrecious) | Personal profile · Minimalistic ✨ | GIF imagery, External statistics cards; useful restraint for first-screen positioning |
| [gkhan205/gkhan205](https://github.com/gkhan205/gkhan205) | Personal profile · Minimalistic ✨ | SVG imagery, External statistics cards; useful restraint for first-screen positioning |
| [pr2tik1/pr2tik1](https://github.com/pr2tik1/pr2tik1) | Personal profile · Minimalistic ✨ | Structured tables; useful restraint for first-screen positioning |
| [DennisHartrampf/DennisHartrampf](https://github.com/DennisHartrampf/DennisHartrampf) | Personal profile · Minimalistic ✨ | SVG imagery, External statistics cards; useful restraint for first-screen positioning |
| [MrStanDu33/MrStanDu33](https://github.com/MrStanDu33/MrStanDu33) | Personal profile · Minimalistic ✨ | Expandable sections, SVG imagery, Generated content markers, External statistics cards; useful restraint for first-screen positioning |
| [jayrajroshan/jayrajroshan](https://github.com/jayrajroshan/jayrajroshan) | Personal profile · Minimalistic ✨ | Plain prose, links or image-led identity; no automation mechanism established from README; useful restraint for first-screen positioning |
| [Ridermansb/Ridermansb](https://github.com/Ridermansb/Ridermansb) | Personal profile · Minimalistic ✨ | SVG imagery; useful restraint for first-screen positioning |
| [maximousblk/maximousblk](https://github.com/maximousblk/maximousblk) | Personal profile · Minimalistic ✨ | Plain prose, links or image-led identity; no automation mechanism established from README; useful restraint for first-screen positioning |
| [AlexMartinFR/AlexMartinFR](https://github.com/AlexMartinFR/AlexMartinFR) | Personal profile · Minimalistic ✨ | Structured tables; useful restraint for first-screen positioning |
| [ChungZH/ChungZH](https://github.com/zirnc/Zirnc) | Personal profile · Minimalistic ✨ | Plain prose, links or image-led identity; no automation mechanism established from README; useful restraint for first-screen positioning; renamed from ChungZH/ChungZH |
| [orhun/orhun](https://github.com/orhun/orhun) | Personal profile · Minimalistic ✨ | GIF imagery, Structured tables; useful restraint for first-screen positioning |
| [Aveek-Saha/Aveek-Saha](https://github.com/Aveek-Saha/Aveek-Saha) | Personal profile · Minimalistic ✨ | External statistics cards; useful restraint for first-screen positioning |
| [Zheeeng/Zheeeng](https://github.com/Zheeeng/Zheeeng) | Personal profile · Minimalistic ✨ | Expandable sections, GIF imagery, External statistics cards; useful restraint for first-screen positioning |
| [tallguyjenks/tallguyjenks](https://github.com/tallguyjenks/tallguyjenks) | Personal profile · Minimalistic ✨ | Generated content markers; useful restraint for first-screen positioning |
| [moertel/moertel](https://github.com/moertel/moertel) | Personal profile · Minimalistic ✨ | Structured tables; useful restraint for first-screen positioning |
| [kha7iq/kha7iq](https://github.com/kha7iq/kha7iq) | Personal profile · Minimalistic ✨ | Plain prose, links or image-led identity; no automation mechanism established from README; useful restraint for first-screen positioning |
| [bilivro/bilivro](https://github.com/bilivro/bilivro) | Personal profile · Minimalistic ✨ | Plain prose, links or image-led identity; no automation mechanism established from README; useful restraint for first-screen positioning |
| [saadeghi/saadeghi](https://github.com/saadeghi/saadeghi) | Personal profile · GIFS 👻 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [ari-hacks/ari-hacks](https://github.com/ari-hacks/ari-hacks) | Personal profile · GIFS 👻 | GIF imagery |
| [Prince-Shivaram/Prince-Shivaram](https://github.com/Prince-Shivaram/Prince-Shivaram) | Personal profile · GIFS 👻 | SVG imagery, GIF imagery |
| [Shanu1515/Shanu1515](https://github.com/Shanu1515/Shanu1515) | Personal profile · GIFS 👻 | GIF imagery |
| [imskr/imskr](https://github.com/imskr/imskr) | Personal profile · GIFS 👻 | SVG imagery, Structured tables |
| [dephraiim/dephraiim](https://github.com/dephraiim/dephraiim) | Personal profile · GIFS 👻 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [demartini/demartini](https://github.com/demartini/demartini) | Personal profile · GIFS 👻 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [sindresorhus/sindresorhus](https://github.com/sindresorhus/sindresorhus) | Personal profile · GIFS 👻 | GIF imagery |
| [Bhard27/Bhard27](https://github.com/0xpranjal/0xpranjal) | Personal profile · GIFS 👻 | GIF imagery, Generated content markers; renamed from Bhard27/Bhard27 |
| [okankocyigit/okankocyigit](https://github.com/okankocyigit/okankocyigit) | Personal profile · GIFS 👻 | GIF imagery |
| [RaghavK16/RaghavK16](https://github.com/RaghavK16/RaghavK16) | Personal profile · GIFS 👻 | SVG imagery, GIF imagery, Structured tables |
| [xrkffgg/xrkffgg](https://github.com/xrkffgg/xrkffgg) | Personal profile · GIFS 👻 | GIF imagery, Structured tables |
| [KevCui/KevCui](https://github.com/KevCui/KevCui) | Personal profile · GIFS 👻 | GIF imagery |
| [muskanrani/muskanrani](https://github.com/muskanrani/muskanrani) | Personal profile · GIFS 👻 | SVG imagery, GIF imagery, External statistics cards |
| [rishavanand/rishavanand](https://github.com/rishavanand/rishavanand) | Personal profile · GIFS 👻 | SVG imagery |
| [KelviNosse/KelviNosse](https://github.com/KelviNosse/KelviNosse) | Personal profile · GIFS 👻 | SVG imagery, GIF imagery, External statistics cards |
| [nilfalse/nilfalse](https://github.com/nilfalse/.github) | Personal profile · GIFS 👻 | GIF imagery, Structured tables; renamed from nilfalse/nilfalse |
| [ShahriarShafin/ShahriarShafin](https://github.com/ShahriarShafin/ShahriarShafin) | Personal profile · GIFS 👻 | Expandable sections, External statistics cards |
| [SP-XD/SP-XD](https://github.com/SP-XD/SP-XD) | Personal profile · GIFS 👻 | Expandable sections, SVG imagery, GIF imagery |
| [kmoroz/kmoroz](https://github.com/kmoroz/kmoroz) | Personal profile · GIFS 👻 | GIF imagery |
| [zackkrida/zackkrida](https://github.com/zackkrida/zackkrida) | Personal profile · Just Images 🎭 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [afc163/afc163](https://github.com/afc163/afc163) | Personal profile · Just Images 🎭 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [thewhiteh4t/thewhiteh4t](https://github.com/thewhiteh4t/thewhiteh4t) | Personal profile · Just Images 🎭 | SVG imagery |
| [akasrai/akasrai](https://github.com/akasrai/akasrai) | Personal profile · Just Images 🎭 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [oussamabouchikhi/oussamabouchikhi](https://github.com/oussamabouchikhi/oussamabouchikhi) | Personal profile · Just Images 🎭 | SVG imagery, External statistics cards, Structured tables |
| [dailyrandomphoto/dailyrandomphoto](https://github.com/dailyrandomphoto/dailyrandomphoto) | Personal profile · Just Images 🎭 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [harish-sethuraman/harish-sethuraman](https://github.com/harish-sethuraman/harish-sethuraman) | Personal profile · Badges 🎫 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [aemmadi/aemmadi](https://github.com/aemmadi/aemmadi) | Personal profile · Badges 🎫 | GIF imagery, External statistics cards |
| [br3ndonland/br3ndonland](https://github.com/br3ndonland/br3ndonland) | Personal profile · Badges 🎫 | SVG imagery |
| [alwinw/alwinw](https://github.com/alwinw/alwinw) | Personal profile · Badges 🎫 | Expandable sections, SVG imagery, External statistics cards |
| [moshfiqrony/moshfiqrony](https://github.com/moshfiqrony/moshfiqrony) | Personal profile · Badges 🎫 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [ileriayo/ileriayo](https://github.com/ileriayo/ileriayo) | Personal profile · Badges 🎫 | SVG imagery, GIF imagery |
| [samujjwaal/samujjwaal](https://github.com/samujjwaal/samujjwaal) | Personal profile · Badges 🎫 | Expandable sections, SVG imagery, External statistics cards |
| [char-al/char-al](https://github.com/char-al/char-al) | Personal profile · Badges 🎫 | Expandable sections, External statistics cards |
| [Coordinate-Cat/Coordinate-Cat](https://github.com/Coordinate-Cat/Coordinate-Cat) | Personal profile · Badges 🎫 | Expandable sections, SVG imagery, GIF imagery, Structured tables |
| [xtenzQ/xtenzQ](https://github.com/xtenzQ/xtenzQ) | Personal profile · Badges 🎫 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [rafi0101/rafi0101](https://github.com/rafi0101/rafi0101) | Personal profile · Badges 🎫 | GIF imagery, External statistics cards |
| [xiaoluoboding/xiaoluoboding](https://github.com/xiaoluoboding/xiaoluoboding) | Personal profile · Fancy Fonts 🖋 | External statistics cards, Structured tables |
| [terrytangyuan/terrytangyuan](https://github.com/terrytangyuan/terrytangyuan) | Personal profile · Icons 🎯 | SVG imagery |
| [hussainweb/hussainweb](https://github.com/hussainweb/hussainweb) | Personal profile · Icons 🎯 | SVG imagery, External statistics cards, Structured tables |
| [peterthehan/peterthehan](https://github.com/peterthehan/peterthehan) | Personal profile · Icons 🎯 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [Thomas-George-T/Thomas-George-T](https://github.com/Thomas-George-T/Thomas-George-T) | Personal profile · Icons 🎯 | SVG imagery |
| [dereknguyen269/dereknguyen269](https://github.com/dereknguyen269/dereknguyen269) | Personal profile · Icons 🎯 | External statistics cards, Structured tables |
| [vbriand/vbriand](https://github.com/vbriand/vbriand) | Personal profile · Icons 🎯 | Plain prose, links or image-led identity; no automation mechanism established from README |
| [BrunnerLivio/BrunnerLivio](https://github.com/BrunnerLivio/BrunnerLivio) | Personal profile · Retro 😎 | SVG imagery, GIF imagery, Structured tables |
| [fnky/fnky](https://github.com/fnky/fnky) | Personal profile · Retro 😎 | SVG imagery, GIF imagery |
| [egorthinks/git-bonsai](https://github.com/egorthinks/git-bonsai) | Git Bonsai · reusable profile tool | GitHub Action setup, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [abhisheknaiidu/todoist-readme](https://github.com/abhisheknaiidu/todoist-readme) | Todoist Stats in Readme · reusable profile tool | GitHub Action setup, Local CLI/generator, Account/token setup; reviewed as an optional pattern, no dependency installed |
| [creativecodeco/gitcard-studio](https://github.com/creativecodeco/gitcard-studio) | GitCard Studio · reusable profile tool | API/image endpoint, Local CLI/generator, Account/token setup, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats) | Github Readme Stats · reusable profile tool | GitHub Action setup, API/image endpoint, Local CLI/generator, Account/token setup, SVG/GIF rendering, Maintenance notice; reviewed as an optional pattern, no dependency installed |
| [dvigo/github-stats](https://github.com/dvigo/github-stats) | GitHub Stats · reusable profile tool | API/image endpoint; reviewed as an optional pattern, no dependency installed |
| [seuthootDev/github-readme-insight-terminal-ascii](https://github.com/seuthootDev/github-readme-insight-terminal-ascii) | Github Readme Insight Terminal Ascii · reusable profile tool | API/image endpoint, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [HwangTaehyun/github-contributor-stats](https://github.com/HwangTaehyun/github-repository-contribution-stats) | Github Contributor Stats · reusable profile tool | API/image endpoint, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed; renamed from HwangTaehyun/github-contributor-stats |
| [flycran/github-gravity](https://github.com/flycran/github-gravity) | GitHub Gravity · reusable profile tool | GitHub Action setup, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [DenverCoder1/github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) | GitHub Streak Stats · reusable profile tool | GitHub Action setup, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [rafaeloliveiraz/gitglance](https://github.com/rafaeloliveiraz/gitglance) | gitglance · reusable profile tool | API/image endpoint, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [simple-icons/simple-icons](https://github.com/simple-icons/simple-icons) | Simple Icons · reusable profile tool | Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [caneco/laravel-github-profile-view-counter](https://github.com/caneco/laravel-github-profile-view-counter) | Laravel GitHub Profile Visit Counter · reusable profile tool | SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [athul/waka-readme](https://github.com/athul/waka-readme) | Dev Metrics in Readme · reusable profile tool | GitHub Action setup, Local CLI/generator, Account/token setup, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [omidnikrah/profile-activity-generator](https://github.com/omidnikrah/profile-activity-generator) | Profile Activity Generator · reusable profile tool | Local CLI/generator; reviewed as an optional pattern, no dependency installed |
| [jojoee/jojoee](https://github.com/jojoee/jojoee) | Current UTC time · reusable profile tool | Markdown generator, embedded media or badge setup documented in README; reviewed as an optional pattern, no dependency installed |
| [jamesgeorge007/github-activity-readme](https://github.com/jamesgeorge007/github-activity-readme) | Github Activity in README · reusable profile tool | GitHub Action setup; reviewed as an optional pattern, no dependency installed |
| [rahuldkjain/github-profile-readme-generator](https://github.com/rahuldkjain/github-profile-readme-generator) | Github Profile README Generator · reusable profile tool | Local CLI/generator, Account/token setup, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [umutphp/github-action-dynamic-profile-page](https://github.com/umutphp/github-action-dynamic-profile-page) | Dynamic Profile Page On Github · reusable profile tool | GitHub Action setup, Local CLI/generator, Account/token setup; reviewed as an optional pattern, no dependency installed |
| [maddhruv/github-readme-npm-downloads](https://github.com/maddhruv/github-readme-npm-downloads) | npm package downloads · reusable profile tool | API/image endpoint; reviewed as an optional pattern, no dependency installed |
| [anmol098/waka-readme-stats](https://github.com/anmol098/waka-readme-stats) | All Dev Stats in Readme · reusable profile tool | GitHub Action setup, API/image endpoint, Local CLI/generator, Account/token setup, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [kittinan/spotify-github-profile](https://github.com/kittinan/spotify-github-profile) | Spotify now playing card generator · reusable profile tool | API/image endpoint, Local CLI/generator, Account/token setup, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [Ileriayo/markdown-badges](https://github.com/Ileriayo/markdown-badges) | Markdown Badges · reusable profile tool | Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [gautamkrishnar/blog-post-workflow](https://github.com/gautamkrishnar/blog-post-workflow) | Latest Blog Posts and StackOverflow activity in readme · reusable profile tool | GitHub Action setup, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [soroushchehresa/github-readme-linkedin](https://github.com/soroushchehresa/github-readme-linkedin) | GitHub Readme LinkedIn · reusable profile tool | API/image endpoint, Local CLI/generator; reviewed as an optional pattern, no dependency installed |
| [omidnikrah/github-readme-medium](https://github.com/omidnikrah/github-readme-medium) | GitHub Readme Medium · reusable profile tool | Markdown generator, embedded media or badge setup documented in README; reviewed as an optional pattern, no dependency installed |
| [omidnikrah/github-readme-stackoverflow](https://github.com/omidnikrah/github-readme-stackoverflow) | GitHub Readme StackOverflow · reusable profile tool | SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [claytonjhamilton/stackoverflow-badge](https://github.com/claytonjhamilton/stackoverflow-badge) | StackOverflow Stats Badge · reusable profile tool | API/image endpoint, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [arturssmirnovs/github-profile-readme-generator](https://github.com/arturssmirnovs/github-profile-readme-generator) | Github Profile README Generator · reusable profile tool | Markdown generator, embedded media or badge setup documented in README; reviewed as an optional pattern, no dependency installed |
| [ABSphreak/readme-jokes](https://github.com/ABSphreak/readme-jokes) | README Jokes · reusable profile tool | API/image endpoint, Local CLI/generator; reviewed as an optional pattern, no dependency installed |
| [ryo-ma/github-profile-trophy](https://github.com/ryo-ma/github-profile-trophy) | GitHub Profile Trophy · reusable profile tool | GitHub Action setup, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [gazf/github-readme-twitter](https://github.com/gazf/github-readme-twitter) | Github Readme Twitter · reusable profile tool | API/image endpoint; reviewed as an optional pattern, no dependency installed |
| [techytushar/random-memer](https://github.com/techytushar/random-memer) | Random Dev Memes · reusable profile tool | Local CLI/generator, SVG/GIF rendering, Maintenance notice; reviewed as an optional pattern, no dependency installed |
| [PiyushSuthar/github-readme-quotes](https://github.com/PiyushSuthar/github-readme-quotes) | GitHub Readme Quotes · reusable profile tool | API/image endpoint, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [rishavanand/github-profilinator](https://github.com/rishavanand/github-profilinator) | GitHub Profilinator · reusable profile tool | Local CLI/generator; reviewed as an optional pattern, no dependency installed |
| [ankurparihar/readme-pagespeed-insights](https://github.com/ankurparihar/readme-pagespeed-insights) | PageSpeed score · reusable profile tool | GitHub Action setup, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [iampavangandhi/Gitwar](https://github.com/iampavangandhi/Gitwar) | Gitwar Profile Score · reusable profile tool | Local CLI/generator, SVG/GIF rendering, Maintenance notice; reviewed as an optional pattern, no dependency installed |
| [khalby786/REHeader](https://github.com/khalby786/REHeader) | Header Images for Github Profile READMEs · reusable profile tool | Local CLI/generator; reviewed as an optional pattern, no dependency installed |
| [DenverCoder1/github-readme-youtube-stats](https://github.com/DenverCoder1/github-readme-youtube-stats) | YouTube Channel Stats · reusable profile tool | Local CLI/generator, Account/token setup, Maintenance notice; reviewed as an optional pattern, no dependency installed |
| [theFr1nge/goodreads-readme](https://github.com/arg3t/goodreads-readme) | Current Book Status from GoodReads · reusable profile tool | API/image endpoint; reviewed as an optional pattern, no dependency installed; renamed from theFr1nge/goodreads-readme |
| [DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) | Readme Typing SVG · reusable profile tool | Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [dahan8473/snake-and-commits](https://github.com/dahan8473/snake-and-commits) | Snake and Commits · reusable profile tool | GitHub Action setup, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [rowkav09/GitHub-profile-stats](https://github.com/rowkavdev/GitHub-profile-stats) | GitHub Profile Stats · reusable profile tool | API/image endpoint, Local CLI/generator; reviewed as an optional pattern, no dependency installed; renamed from rowkav09/GitHub-profile-stats |
| [starlash7/github-candles](https://github.com/starlash7/github-candles) | github-candles · reusable profile tool | GitHub Action setup, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [in-c0/daily-badge](https://github.com/in-c0/daily-badge) | Daily Badge · reusable profile tool | GitHub Action setup, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [0xharkirat/dither-portrait](https://github.com/0xharkirat/dither-portrait) | Dither Portrait · reusable profile tool | GitHub Action setup, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [seuthootDev/github-readme-zodiac](https://github.com/seuthootDev/github-readme-zodiac) | GitHub Readme Zodiac · reusable profile tool | GitHub Action setup, API/image endpoint, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [seuthootDev/github-readme-chinese-zodiac](https://github.com/seuthootDev/github-readme-chinese-zodiac) | GitHub Readme Chinese Zodiac · reusable profile tool | API/image endpoint, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [icortesb/vinilo](https://github.com/icortesb/vinilo) | vinilo · reusable profile tool | GitHub Action setup, Local CLI/generator, Account/token setup, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed |
| [prsdx/github-pet](https://github.com/knowprasad/YourTomo) | Github Pet · reusable profile tool | GitHub Action setup, Local CLI/generator, SVG/GIF rendering; reviewed as an optional pattern, no dependency installed; renamed from prsdx/github-pet |
