-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u3
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mar 17 Novembre 2020 à 14:59
-- Version du serveur :  5.5.60-0+deb8u1
-- Version de PHP :  5.6.36-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `saintdi26u_3`
--

-- --------------------------------------------------------

--
-- Structure de la table `immo_biens`
--

CREATE TABLE IF NOT EXISTS `immo_biens` (
`idb` int(11) NOT NULL,
  `nomb` varchar(30) NOT NULL,
  `mediab` varchar(30) NOT NULL,
  `categorieb` int(11) NOT NULL,
  `prixb` bigint(20) DEFAULT NULL,
  `codeenergieb` varchar(1) NOT NULL,
  `indiceenergieb` int(11) NOT NULL,
  `surfaceb` bigint(20) NOT NULL,
  `chambreb` bigint(20) DEFAULT NULL,
  `descb` varchar(1000) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

--
-- Contenu de la table `immo_biens`
--

INSERT INTO `immo_biens` (`idb`, `nomb`, `mediab`, `categorieb`, `prixb`, `codeenergieb`, `indiceenergieb`, `surfaceb`, `chambreb`, `descb`) VALUES
(1, 'Natura', 'maison_1.jpg', 2, 180000, 'A', 80, 180, 7, 'Grande surface habitable, plancher haut traditionnel permettant une exploitation optimum des combles qui sont ici aménagés en suite parentale'),
(2, 'Matinale', 'maison_2.jpg', 2, 232000, 'B', 71, 160, 6, 'Maison contemporaine qui puise son originalité dans sa forme et sa toiture. Grands espaces de vie et combles aménagés'),
(3, 'Méridienne', 'maison_3.jpg', 3, 210000, 'B', 74, 170, 7, 'Maison contemporaine qui puise son originalité dans sa forme et sa toiture. Grands espaces de vie et combles aménagés'),
(4, 'Ariane', 'maison_4.jpg', 3, 225000, 'A', 85, 210, 8, 'Grande maison à 2 volumes séjour/chambres, à ½ niveau intérieur et extérieur pour privilégier chaque espace de vie.'),
(5, 'Zénith', 'maison_5.jpg', 1, 197000, 'C', 62, 230, 8, 'Grande maison construite en L, avec pignon avancé et croupe de toit. Linteaux lorrains avec sous-sol semi enterré.'),
(6, 'Equateur', 'maison_6.jpg', 1, 280000, 'C', 69, 200, 7, 'Grande maison de plein pied en L à combles. Le garage traversant est dans le volume de la maison. Un vaste comble est à aménager.'),
(7, 'Alyzée', 'maison_7.jpg', 1, 250000, 'A', 90, 155, 5, 'Pignon en décroché, avec combles aménageables ou totalement aménagés, cette maison bien structurée propose un garage en sous-sol.'),
(8, 'Estivale', 'maison_8.jpg', 2, 199000, 'B', 79, 160, 5, 'De plus de 140 m² habitables, cette maison contemporaine est disponible avec ou sans terrasse. L''agencement du rez-de-chaussée vous apportera bien-être et convivialité grâce à sa suite parentale avec dressing et salle d''eau privative, son wc indépendant et sa cuisine ouverte sur le vaste salon/séjour lumineux.'),
(9, 'Rubix house', 'maison_9.jpg', 1, 205000, 'B', 78, 185, 5, 'Deux chambres, une salle de bain avec wc indépendant ainsi qu''une mezzanine prennent place à l''étage. Pour un plus grand confort, le garage bénéficie d''un accès direct à la maison par le cellier.'),
(10, 'Lego house', 'maison_10.jpg', 1, 197000, 'A', 93, 200, 6, 'Lignes originales, architecture contemporaine : vous serez séduit par ce modèle offrant de beaux et grands volumes de vie.'),
(11, 'Cornaline', 'maison_11.jpg', 2, 280000, 'B', 76, 220, 7, 'Avec sa forme insolite, l''espace de vie vous offre de multiples possibilités d''aménagement : partie salon, partie séjour, coin cuisine ... '),
(12, 'Jade', 'maison_12.jpg', 2, 250000, 'A', 89, 195, 7, 'Avec ses 3 grandes baies vitrées dans la pièce principale, cette maison contemporaine est littéralement baignée de lumière.'),
(13, 'Opaline', 'maison_13.jpg', 3, 199000, 'B', 76, 190, 6, 'La suite parentale avec salle d''eau privative prend place au rez-de-chaussŽe. Trois autres chambres, dont une avec dressing, occupent l''Žtage.'),
(14, 'Diamant', 'maison_14.jpg', 3, 205000, 'B', 75, 160, 5, 'maginez votre futur pavillon de plain pied comprenant 3 chambres, une grande pièce de vie, un garage et un cellier'),
(15, 'Rubis', 'maison_15.jpg', 3, 178000, 'A', 90, 185, 6, 'Ce bâtiment se distingue par son milieu intérieur sain, son efficacité énergétique, son utilisation des énergies renouvelables, sa faible incidence sur l’environnement, le grand soin apporté à la conservation des ressources et son abordabilité.'),
(16, 'Nacre', 'maison_16.jpg', 3, 239000, 'C', 63, 200, 7, 'La maison comprend, autour de l’escalier à vis, une pièce principale, et 3 chambres placées les unes au dessus des autres. Chaque pièce mesure environ 30m2 et a une vue imprenable sur le village, la vallée de l’Aveyron, ou le château de Najac.'),
(17, 'Harmony', 'maison_17.jpg', 3, 305000, 'C', 65, 220, 9, 'Accès direct au jardin depuis toutes les pièces de la maison. Espace intérieur très fonctionnel : les parties jour/nuit sont nettement séparées. Une maison sans escalier : accessibilité et circulation fluide'),
(18, 'Aurore', 'maison_18.jpg', 2, 244000, 'A', 84, 195, 7, 'Une surface habitable plus grande (surtout si vous disposez d’un petit terrain). Un rez-de-chaussée réservé aux pièces communes et l''étage aux chambres. Possibilité de concevoir une architecture vraiment personnalisée'),
(19, 'Boréale', 'maison_19.jpg', 1, 276000, 'B', 71, 190, 6, 'Une surface habitable évolutive en aménagement les combles dans un deuxième temps, pas besoin de déménager. Une maison où le charme opère : plafonds rampants, poutres apparentes. Nombreuses possibilités d’aménagement de l’espace de l’étage'),
(20, 'Equinoxe', 'maison_20.jpg', 3, 254000, 'B', 79, 170, 6, 'Le grenier déjà équipé d''un plancher et de deux  fenêtres  vélux  est accessible par une échelle de meunier et peut-être  encore aménagé. Le sous-sol se compose d''un espace rangement , d''une pièce chauffée, entièrement insonorisée, destinée à la pratique de la musique,  une salle  de gym et  salle de  ping pong.'),
(21, 'Tropique', 'maison_21.jpg', 2, 198000, 'A', 92, 200, 7, 'Installation domotique haut de gamme telle qu''une alarme centralisée, 14 volets roulants à programmation centralisée, portail radio commandé,  un arrosage automatique enterré. Un garage de 26 m2 avec porte électrique complète le tout. Deux autres places de parking sont possibles dans la cour.');

-- --------------------------------------------------------

--
-- Structure de la table `immo_categories`
--

CREATE TABLE IF NOT EXISTS `immo_categories` (
`idc` int(11) NOT NULL,
  `nomc` varchar(50) NOT NULL,
  `descc` varchar(500) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Contenu de la table `immo_categories`
--

INSERT INTO `immo_categories` (`idc`, `nomc`, `descc`) VALUES
(1, 'Modernité', 'Des maisons pensées pour les familles, faciles à vivre, intégrant toutes les fonctionnalités les plus récentes en termes de domotique, de recyclage des calories. Construite conformément aux dernières normes en vigueur sur l''économie d''énergie et les matériaux recyclables, votre maison vous assure une qualité de vie irréprochable pour longtemps.'),
(2, 'Tradition', 'Vous souhaitez rester fidèles aux traditions et au style de votre région, ces maisons sont faites pour vous ! Nos architectes s''engagent à respecter toutes les contraintes techniques et environnementales de votre commune tout en vous garantissant des espaces vastes, fonctionnels, ouverts. La tradition respectée avec tout le modernisme de matériaux et les techniques de construction les plus récentes...'),
(3, 'Design', 'Nos maisons sont modernes, tendances, originales... des havres de paix et de lumière pour toute votre famille. Le style design se plie à toutes les contraintes de volumes, de circulation tout en intégrant les normes BBC de construction les plus performantes. Modulaires et évolutives, nos maisons design resteront modernes pour longtemps !');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `immo_biens`
--
ALTER TABLE `immo_biens`
 ADD PRIMARY KEY (`idb`);

--
-- Index pour la table `immo_categories`
--
ALTER TABLE `immo_categories`
 ADD PRIMARY KEY (`idc`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `immo_biens`
--
ALTER TABLE `immo_biens`
MODIFY `idb` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT pour la table `immo_categories`
--
ALTER TABLE `immo_categories`
MODIFY `idc` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
