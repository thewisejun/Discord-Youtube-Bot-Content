-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 04, 2021 at 05:26 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `youtube`
--

-- --------------------------------------------------------

--
-- Table structure for table `discord`
--

CREATE TABLE `discord` (
  `id` int(11) NOT NULL,
  `discordid` varchar(256) NOT NULL,
  `points` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `discord`
--

INSERT INTO `discord` (`id`, `discordid`, `points`) VALUES
(77, '824119035721285704', 133),
(78, '390593253457526794', 0),
(79, '803150807348412426', 0),
(80, '799888892274802698', 0),
(81, '393158360519802910', 0),
(82, '789155884353060936', 0),
(83, '508725561036636173', 1),
(85, '741634961609588737', 0),
(87, '821639110992330763', 0),
(88, '472383584175390723', 0),
(89, '563080589905887232', 0),
(90, '404365332912930827', 0),
(91, '690455088824582174', 0),
(92, '793988237592756225', 0),
(93, '736376770504425492', 0),
(96, '379648407020634112', 0),
(97, '374708558446592000', 0),
(98, '793100948616511499', 0),
(99, '739166812717187116', 0),
(100, '742578272688275467', 0),
(101, '245699664454615050', 0),
(102, '572243228112453636', 0),
(104, '771400730237993000', 0),
(105, '163337136622403584', 0),
(106, '260620702300766210', 0),
(107, '234073975515250688', 0),
(108, '612186573014040577', 0),
(109, '734983876618748004', 0),
(110, '711443505339170898', 0),
(111, '818179451719516200', 0),
(113, '235148962103951360', 0),
(114, '251138381281624065', 0),
(115, '323385745358192640', 0),
(116, '680625010389549174', 0),
(117, '704885447251329054', 0),
(118, '729915043017392148', 0),
(119, '340550425256132613', 0),
(121, '254382469845876736', 7),
(122, '442418653179281408', 0),
(123, '819361576054292483', 0),
(124, '422128974215380992', 0),
(126, '510129926322782246', 0),
(128, '314230903872421889', -9),
(129, '342738297270960128', 19),
(130, '232637764796022784', 0),
(131, '288810135285923840', 0),
(132, '789594055868416010', 0),
(134, '190293711647670272', 0),
(135, '652908535323295774', 0),
(136, '409875566800404480', 0),
(137, '614882019230351361', 0),
(138, '723351017126756443', 1),
(139, '295516887402414080', 0),
(140, '461492419150479389', 0),
(141, '804720923939700737', 0),
(142, '495622392475811863', 0),
(143, '257099089269882880', 2),
(145, '411312401925799946', 0),
(146, '765197462922854400', 0),
(147, '788805131654529025', 0),
(148, '412790610777473025', 0),
(149, '302050872383242240', 0),
(153, '401211820238438411', 0),
(161, '289466117628493827', 0),
(162, '485952639423741984', 0),
(163, '759433582107426816', 1),
(164, '407218405360533544', 1),
(165, '451436337866866689', 0),
(166, '684431070690934855', 0),
(168, '374728098123481090', 0),
(172, '807725015444488233', 0),
(175, '525085428445872267', 0),
(178, '584319130199523338', 0),
(179, '658434453873360906', 0),
(187, '289864624545988618', 0),
(188, '724604631551967274', 0),
(194, '809543914129588305', 0),
(196, '518939846367248434', 0),
(199, '501015134479712257', 0),
(200, '471368871408828436', 0),
(201, '346026344674492416', 0),
(202, '724001677761314837', 2),
(203, '676519314106613785', 2),
(211, '775723571409846292', 0),
(217, '797103066905837608', 0),
(225, '513468477923917844', 0),
(227, '341843958739238912', 0),
(228, '756060673695416360', 0),
(229, '768138481179295774', 0),
(232, '732098792320401500', 0),
(233, '777060055211835412', 0),
(235, '819451914365698100', 0),
(239, '733075015481950248', 0),
(240, '698457401115934782', 0),
(242, '719705579861573744', 0),
(243, '801308599640129547', 0),
(244, '809764602803912765', 6),
(245, '781195982956265562', 0),
(246, '820922506499194961', 0),
(248, '749981800188608542', 0),
(249, '745286535687176242', 0),
(250, '798268176143089694', 0),
(253, '525377490466897940', 0),
(254, '496470766444085248', 0),
(258, '770175082503864350', 1),
(259, '791778587040022588', 0),
(263, '474668178815844373', 0),
(265, '745393995777048697', 0),
(268, '785621706894868480', 0),
(271, '356541665118519306', 0),
(272, '804145790104371251', 0),
(276, '705743321972080681', 5),
(282, '484918194465669174', 0),
(283, '711612686525399070', 0),
(284, '812911449046384651', 0),
(285, '712906478943469580', 6),
(296, '645213629591060481', 0),
(297, '774874871607984138', 0),
(298, '461250264997953546', 0),
(299, '711218726955122731', 0),
(301, '335559152770351104', 0),
(306, '817100337461985280', 0),
(307, '683459528284700706', 1),
(314, '777174560998817812', 0),
(331, '447563047775764480', 0),
(336, '806175376765616220', 0),
(337, '813479148676186173', 0),
(338, '284286909302308866', 0),
(340, '819690402353381406', 0),
(341, '521053507130753054', 4),
(347, '828307499643568138', 0),
(349, '817969431979884586', 0),
(351, '247905646396047362', 0),
(353, '759394871076192276', 3),
(354, '649549219996237834', 0),
(358, '754919453225123860', 0),
(362, '816687893301035008', 0),
(364, '796304908243697664', 0),
(365, '627852717020282936', 1),
(367, '761808159819563028', 0),
(368, '247154392225021954', 2),
(370, '185816772669079552', 2),
(371, '799637031650852874', 0),
(372, '609869222503251978', 1),
(373, '598117428286717952', 4),
(375, '305333317560172544', 12),
(376, '423951507319422987', 0),
(377, '811605146055475221', 0),
(378, '757647315593855026', 0),
(382, '629947899932835840', 0),
(383, '805518016262701096', 1),
(384, '822949151355699301', 0),
(385, '456953350978535425', 10),
(386, '344129058382282752', 0),
(387, '746900111870656607', 0),
(391, '639008840876163074', 0),
(393, '700311185664376863', 0),
(397, '676904472965808168', 0),
(398, '789301124766892102', 0),
(399, '821088072103624796', 0),
(400, '781321674514759732', 0),
(401, '644185833116663809', 0),
(404, '645356323571105802', 0),
(405, '358579923159351326', 0),
(407, '711635319908466780', 0),
(408, '817460597675130890', 0),
(409, '821825494416097290', 3),
(411, '573323091363627016', 0),
(413, '553997319884767250', 4),
(414, '812261220371005482', 0),
(415, '453052194137178132', 0),
(416, '510981184080052235', 0),
(417, '805148895520096307', 0),
(419, '721923604064895018', 0),
(420, '724508735535448095', 0),
(425, '741814727633666068', 0),
(426, '766740314052362250', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `discord`
--
ALTER TABLE `discord`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `discord`
--
ALTER TABLE `discord`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=431;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
